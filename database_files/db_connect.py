import MySQLdb
from sqlalchemy import create_engine

class SQL_connect:

    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = MySQLdb.connect(host='localhost',
                                user = 'root',
                                passwd = '12qwaszx')

        self.curr = self.conn.cursor()

    def execute(self, command):
        if not 'self.curr' in locals():
            self.connect()

        try:
            self.curr.execute(command)

        except Exception as e:
            print (e)

    def commit(self):
        try:
            self.conn.commit()
            self.conn.close()

        except Exception as e:
            print (e)
