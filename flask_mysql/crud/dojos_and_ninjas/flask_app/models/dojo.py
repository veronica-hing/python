# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the Dojo table from our database
# ninja is dependent on dojo so we'll also have to include ninjas
from flask_app.models import ninja
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #this will be the list of ninjas we get when we show the dojo page
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) "
        query = query + "VALUES ( %(name)s, NOW(), NOW());"
        id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return id

    @classmethod
    def get_one(cls, id):
            query = "SELECT * FROM dojos WHERE id = %(id)s ;"
            data = {"id": id}
            result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
            result = result[0]
            dojo = Dojo(result)
            return dojo

    @classmethod
    def get_dojo_with_ninjas(cls, id):
        #left join so that even empty dojos have a table shown
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s ;"
        data = {"id": id}
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        #check to see if dojo is empty first before doing extra work
        if not results[0]["ninjas.id"]:
            return dojo
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"],
                "dojo_id": row_from_db["dojo_id"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo