from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create_dojo(cls, data_dict):
        query = """INSERT INTO dojos (name) VALUES (%(name)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for row in results:
            dojo =  cls(row)
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def get_dojos_ninja(cls, data_dict):
        query = """SELECT ninjas.id, first_name, last_name, age FROM ninjas JOIN dojos on ninjas.dojo_id = dojos.id WHERE dojo_id=%(dojo_id)s;"""
        results = connectToMySQL(DATABASE).query_db(query,data_dict)
        return results
    
    @classmethod
    def get_dojo_by_id(cls, data_dict):
        query = """SELECT * FROM dojos WHERE id=%(dojo_id)s;"""
        results = connectToMySQL(DATABASE).query_db(query,data_dict)
        return cls(results[0])