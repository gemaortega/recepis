import pymysql.cursors

from flask_app.config.constants import DB_HOST, DB_USER, DB_PASSWORD


class MySQLConnection:
    """
    This class will give us an instance of a connection to our database
    """
    def __init__(self, db):
        connection = pymysql.connect(host=DB_HOST,
                                     user=DB_USER,
                                     password=DB_PASSWORD,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)
        # establish the connection to the database
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() 


def connect_to_mysql(db):
    """
    Receives the database we're using and uses it to create an instance of MySQLConnection
    :param db: database
    :return: MySQLConnection instance
    """
    return MySQLConnection(db)
