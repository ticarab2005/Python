from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under30 = data["under30"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes(name,description,instructions,date_made,under30,user_id) VALUES (%(name)s, %(description)s,%(instructions)s,%(date_made)s,%(under30)s,%(user_id)s)"
        return connectToMySQL("recipes_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes_schema").query_db(query)
        recipes = []
        
        for n in results:
            print(n['date_made'])
            recipes.append(cls(n))
        return recipes

    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under30=%(under30)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("recipes_schema").query_db(query,data)
        
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete_recipe(cls,data):
        query = "Delete from recipes WHERE id = %(id)s"
        return connectToMySQL("recipes_schema").query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 3:
            flash("Name must be 3 characters long")
            is_valid = False
        if len(recipe["instructions"]) < 3:
            flash("Instructions must be 3 characters long")
            is_valid = False
        if len(recipe["description"]) < 3:
            flash("Description must be 3 characters long!")
            is_valid = False
        if len(recipe["date_made"]) < 1:
            flash("Must pick a date!")
            is_valid = False
        return is_valid
