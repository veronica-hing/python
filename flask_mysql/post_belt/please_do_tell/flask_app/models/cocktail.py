from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash

DATABASE = 'pdt_erd'
 
class Recipe:
    def __init__(self, data):
        self.id = data["idDrink"]
        self.name = data["strDrink"]
        self.thumb = data["StrDrinkThumb"]
        self.glass = data["StrGlass"]
        self.ingredients = data["ingredients_arr"]#need to do some formatting before putting info in
        self.instructions = data["instructions"]
        self.ing_meas = data["meas_arr"]#formatted like self.ingredients
        self.created_at = data["created_at"] # maybe used when user can create recipe
        self.updated_at = data["updated_at"] # maybe used when user can create recipe 
        self.users_id = data["users_id"]     # maybe used when user can create recipe, just used for favoriting purposes for now
    
    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO recipes (name, description, instruction, is_quick, made_at, created_at, updated_at, users_id)"
    #     query = query + " VALUES (%(name)s, %(description)s, %(instruction)s, %(is_quick)s, %(made_at)s, NOW(), NOW(), %(users_id)s);"
    #     recipe_id = connectToMySQL(DATABASE).query_db(query, data)
    #     return recipe_id

    @classmethod
    def get_favorites(cls, data): #interacts with our db to get list of favorites
        query = "SELECT * FROM favorites WHERE users_id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query,data)
        # Create an empty list to append our instances of cocktails to call
        cocktails = []
        # Iterate over the db results and create instances of cocktail with cls.
        for row in results:
            #need to call the API for each favorite, so maybe move this chunk to controller
            ingredients_arr = []#list of ingredients since in API keys for each ingredient is formatted strIngredient1...15
            meas_arr = []#same as above but for strMeasure1...15
            for i in range(1,16):
                if(row[f'strIngredient{i}'] is 'null'):
                    break
                else:
                    ingredients_arr.push(row[f'strIngredient{i}'])
                    meas_arr.push(row[f'strMeasure{i}'])
            ##both ingredients_arr and meas_arr are populated now
            cocktail_data = {
                "id" = row["idDrink"],
                "name" = row["strDrink"],
                "thumb" = row["StrDrinkThumb"],
                "glass" = row["StrGlass"],
                "ingredients" = ingredients_arr, #formatted in above for loop
                "instructions" = row["instructions"],
                "ing_meas" = meas_arr, #formatted like self.ingredients
                "created_at" = row["created_at"], # maybe used when user can create recipe
                "updated_at" = row["updated_at"], # maybe used when user can create recipe 
                "users_id" = row["id"], #user id of the favorite list we're getting    
            }
            cocktails.append( cls(cocktail_data) )
        return recipes

    # @classmethod probably call directly from controller since interacting with API
    # def get_one(cls, data):
    #     query = "SELECT * FROM recipes WHERE id = %(id)s;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     # get the first one from results and turn it into recipe
    #     return cls(results[0])

##implement this functionality later in DB
    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM recipes WHERE id = %(id)s;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, is_quick = %(is_quick)s, updated_at = NOW(), made_at = %(made_at)s WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)