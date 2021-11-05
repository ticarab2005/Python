from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data["id"],
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_cr").query_db(query)
        users = []

        for r in results:
            users.append(cls(r))
        return users

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) VALUE(%(first_name)s,%(last_name)s,%(email)s)"
        result = connectToMySQL("users_cr").query_db(query,data)
        return result
    
    @classmethod
    def create(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
        user = connectToMySQL("users_cr").query_db(query,data)
        return cls(user)
    
    @classmethod
    def create(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        user = connectToMySQL("users_cr").query_db(query,data)
        return cls(user)

