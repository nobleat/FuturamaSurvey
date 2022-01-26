from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "dojo_survey_schema"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.location = data['location']
        self.character = data['favorite_character']
        self.episode = data['episode']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (first_name, last_name, location, favorite_character, episode) VALUES (%(first_name)s, %(last_name)s, %(location)s, %(favorite_character)s, %(episode)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result

    @staticmethod
    def validate_user(user):
        is_valid=True
        if len(user['first_name'])<3:
            flash("Name must be at least 3 characters.")
            is_valid=False
        if len(user['last_name']) <3:
            flash("Name must be at least 3 characters.")
            is_valid=False
        return is_valid