# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) "
        query = query + "VALUES ( %(fname)s, %(lname)s, %(email)s, NOW(), NOW() );"

        testy = connectToMySQL('users_schema').query_db(query, data)
        print(testy)
        return testy

    @classmethod
    def edit(cls, data):
        query = "UPDATE users "
        query = query + "SET first_name = %(first_name)s, last_name = %(last_name)s, email =  %(email)s, updated_at = NOW() "
        query = query + "WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query ="DELETE FROM users WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s ;"
        data = {"id": id}
        result =  connectToMySQL('users_schema').query_db(query, data)
        #get the first dictionary from the list
        result = result[0]
        user = User(result)
        return user
            