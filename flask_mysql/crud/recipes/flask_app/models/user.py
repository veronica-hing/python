# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the Dojo table from our database
# ninja is dependent on dojo so we'll also have to include ninjas
from flask_app.models import recipe
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{6,}$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.hashed_pw = data['hashed_pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #this will be the list of ninjas we get when we show the dojo page
        self.recipes = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_erd').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL('recipes_erd').query_db(query, data)

        if not user:
            return False
        return user[0]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users ( first_name, last_name, email, hashed_pw, created_at, updated_at) "
        query = query + "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(hashed_pw)s, NOW(), NOW());"
        id = connectToMySQL('recipes_erd').query_db(query, data)
        return id

    @staticmethod
    def validate_user(user):
        is_valid = True

        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not PASSWORD_REGEX.match(user['pw']): 
            flash("Password needs to be at least 6 characters with lower and capital letters and special characters")
            is_valid = False
        if not (user['pw'] == user['pw_confirm']):
            is_valid = False
            flash("Password needs to match confirmation")
        return is_valid

    @staticmethod
    def validate_login(email):
        is_valid = True
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_user_with_recipes(cls, id):
        #left join so that even users with no recipes are shown
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.users_id = users.id WHERE users.id = %(id)s ;"
        data = {"id": id}
        results = connectToMySQL('recipes_erd').query_db(query, data)
        print(results)
        user = cls(results[0])
        #check to see if user has no recipes before doing extra work
        if not results[0]["recipes.id"]:
            return user
        for row_from_db in results:
            recipe_data = {
                "id": row_from_db["recipes.id"],
                "name": row_from_db["name"],
                "description": row_from_db["description"],
                "instruction": row_from_db["instruction"],
                "is_quick": row_from_db["is_quick"],
                "made_at": row_from_db["made_at"],
                "created_at":row_from_db["recipes.created_at"],
                "updated_at":row_from_db["recipes.updated_at"],
                "users_id": row_from_db["users_id"]
            }
            user.recipes.append(recipe.Recipe(recipe_data))
        return user