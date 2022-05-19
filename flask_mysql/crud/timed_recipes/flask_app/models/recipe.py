from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash

DATABASE = 'recipes_erd'
 
class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.is_quick = data["is_quick"]
        self.made_at = data["made_at"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["users_id"]
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, is_quick, made_at, created_at, updated_at, users_id)"
        query = query + " VALUES (%(name)s, %(description)s, %(instruction)s, %(is_quick)s, %(made_at)s, NOW(), NOW(), %(users_id)s);"
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, data)
        # get the first one from results and turn it into recipe
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, is_quick = %(is_quick)s, updated_at = NOW(), made_at = %(made_at)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)