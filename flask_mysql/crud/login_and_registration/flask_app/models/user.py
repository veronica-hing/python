from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{6,}$') 
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.pw = data["pw"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw, created_at, updated_at)"
        query = query + " VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s, NOW(), NOW());"
        user_id = connectToMySQL('login_and_reg').query_db(query, data)
        return user_id

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL('login_and_reg').query_db(query, data)
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
        if not PASSWORD_REGEX.match(user['pw']): 
            flash("Password needs to be at least 6 characters with lower and capital letters and special characters")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(email):
        is_valid = True
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid