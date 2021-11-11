from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails(email,created_at,updated_at) VALUES(%(email)s, NOW(),NOW())"
        return connectToMySQL("email_schema").query_db(query,data)


    @classmethod
    def get_all_email(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("email_schema").query_db(query)
        emails = []

        for r in results:
            emails.append(cls(r))
        return emails

    @classmethod
    def delete_email(cls,data):
        query = "DELETE from emails WHERE id = %(id)s"
        return connectToMySQL("email_schema").query_db(query,data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("email_schema").query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken, try again.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid
