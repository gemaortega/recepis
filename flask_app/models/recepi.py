from flask_app.config.constants import DB_SCHEMA
from flask_app.config.mysqlconnection import connect_to_mysql


class Recepi:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data ['description']
        self.instructions = data ['instrucions']
        self.under_thirty = data ['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def created(cls, data):
        query = "INSERT INTO recepis (name) VALUES (%(name)s);"
        result = connect_to_mysql(DB_SCHEMA).query_db(query, data)
        return result

    @classmethod
    def all_recepis(cls):
        query = "SELECT * FROM recepis;"
        result = connect_to_mysql(DB_SCHEMA).query_db(query)
        recepis = []
        for recepi in result:
            recepis.append(cls(recepi))
        return recepis

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM recepis WHERE id = %(id)s;"
        result = connect_to_mysql(DB_SCHEMA).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_users_with_recepi(cls, data):
        consulta = """SELECT * FROM users JOIN recepis ON users.recepi_id = recepis.id WHERE recepis.id = %(id)s;"""
        result = connect_to_mysql(DB_SCHEMA).query_db(consulta, data)
        return result
