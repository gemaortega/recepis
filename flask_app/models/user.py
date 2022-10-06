from flask import flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app.config.constants import DB_SCHEMA
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True # asumimos que esto es true
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['email']) < 8:
            flash("email must be at least 8 charactes.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'register')
            is_valid = False
        if len(user['password']) < 6:
            flash("password must be at least 6 characters.", 'register')
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords do not match!", "register")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        #query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        query = """INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connect_to_mysql(DB_SCHEMA).query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connect_to_mysql(DB_SCHEMA).query_db(query, data)
        # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

