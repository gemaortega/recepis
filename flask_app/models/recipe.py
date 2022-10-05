from datetime import date, datetime
from flask_app.config.constants import DB_SCHEMA
from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data ['description']
        self.instructions = data ['instructions']
        self.under_thirty = data ['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @staticmethod
    def validate_recepi(user):
        is_valid = True # asumimos que esto es true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.", 'new_recepi')
            is_valid = False
        if len(user['description']) < 1:
            flash("Description must not be blank.", 'new_recepi')
            is_valid = False
        if len(user['instructions']) < 1:
            flash("Instructions must not be blank.", 'new_recepi')
            is_valid = False
        return is_valid

    @classmethod
    def created(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, under_thirty, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under)s, %(user_id)s);
        """
        result = connect_to_mysql(DB_SCHEMA).query_db(query, data)
        return result

    @classmethod
    def all_recipes_with_user(cls):
        """
            Returns a list with all recipes and their author (user_name, user_id) as dictionaries.
        """
        query = "SELECT u.id AS user_id, u.first_name AS user_name, r.* FROM recipes AS r JOIN users AS u ON u.id = r.user_id;"
        result = connect_to_mysql(DB_SCHEMA).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(recipe)
        return recipes

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connect_to_mysql(DB_SCHEMA).query_db(query, data)
        return cls(result[0])
