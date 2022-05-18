# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the recipes table

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.is_quick = data['is_quick']
        self.made_at = data['made_at']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id'] #this user_id is the author of the recipe

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_erd').query_db(query)
        # Create an empty list to append our instances of users
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes ( name, description, instruction, is_quick, made_at, created_at, updated_at, users_id) "
        query = query + "VALUES ( %(name)s, %(description)s, %(instruction)s, %(is_quick)s, %(made_at)s, NOW(), NOW(), %(users_id)s);"
        id = connectToMySQL('recipes_erd').query_db(query, data)
        return id

    @classmethod
    def get_by_id(cls,id):
        query = "SELECT * FROM recipes WHERE id = %(id)s ;"
        data = {"id": id}
        recipe = connectToMySQL('recipes_erd').query_db(query,data)
        return recipe[0] #this is a dictionary