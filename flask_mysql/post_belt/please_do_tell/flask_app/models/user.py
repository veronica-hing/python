from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash
#from flask_app.models import recipe
import re

DATABASE = 'recipes_erd'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{6,}$') 
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.user_name = data["user_name"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.hashed_pw = data["hashed_pw"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (user_name, first_name, last_name, email, hashed_pw, created_at, updated_at)"
        query = query + " VALUES (%(user_name)s, %(first_name)s, %(last_name)s, %(email)s, %(hashed_pw)s, NOW(), NOW());"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL(DATABASE).query_db(query, data)
        if not user:
            return False
        return user[0]

    @classmethod
    def get_by_user_name(cls,data):
        query = "SELECT * FROM users WHERE user_name = %(user_name)s;"
        user = connectToMySQL(DATABASE).query_db(query, data)
        if not user:
            return False
        return user[0]

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
        if not PASSWORD_REGEX.match(user['hashed_pw']): 
            flash("Password needs to be at least 6 characters with lower and capital letters and special characters")
            is_valid = False
        if not user['hashed_pw'] == user['confirm_pw']:
            flash("Please confirm password")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(email):
        is_valid = True
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid