import MySQLdb
from db_connect import SQL_connect
from make_table_command import *
import pandas as pd
import os
from sqlalchemy import create_engine


class DB_Handler:

    def __init__(self):
        self.db = SQL_connect()

    def create_database(self):
        """ set up database """
        create_tennis_database = """CREATE DATABASE tennis_data;"""
        self.db.execute(create_tennis_database)
        self.db.commit()

    def create_tables(self):
        ''' Create all tables from sql commands '''

        use_tennis = """USE tennis_data;"""
        self.db.execute(use_tennis)

        sql_command = """CREATE TABLE %s"""
        tennis_matches_tables = sql_command % (atp_matches_1968_2017)
        players_table = sql_command % (players)
        player_ranking_table = sql_command % (player_rankings)

        self.db.execute(tennis_matches_tables)
        self.db.execute(players_table)
        self.db.execute(player_ranking_table)

        self.db.commit()

    def get_file_list(self):

        l = os.listdir(os.path.abspath('../tennis_atp'))
        return l

    def what_table(self, f):

            ''' Sorting file by substrings '''

            if 'atp_matches' in f:
                return 'atp_matches_1968_2017'

            elif 'atp_ranking' in f:
                return 'player_rankings'

            elif 'atp_player' in f:
                return 'players'

            else:
                print ('Dont need this file')
                return None


    def load_csv(self):
        ''' Load CSVs into correct databases '''

        engine = create_engine('mysql+mysqldb://root:12qwaszx@localhost/tennis_data')
        path = os.path.abspath('../tennis_atp') + '/'
        files = self.get_file_list()

        for f in files:
            table = self.what_table(f)
            if table:
                if table is not 'atp_matches_1968_2017':
                    df = self.add_headers(f, table)
                    print (table)
                    print (df)
                    df.to_sql(con=engine, name=table, index=False, if_exists='append')

                else:
                    df = pd.read_csv(path+f)
                    df.to_sql(con=engine, name=table, index=False, if_exists='append')



        #df.to_sql(con=con, name='table_name_for_df', if_exists='replace', flavor='mysql')

    def add_headers(self, f, table):

        path = os.path.abspath('../tennis_atp') + '/'
        if 'player_ranking' in table:
            df = pd.read_csv(path+f, names=players_rankings_header)
            return df

        elif 'players' in table:
            df = pd.read_csv(path+f, names=players_header)
            return df

        else:
            print ('none')


    def drop_database(self):
        self.db.execute("""DROP database tennis_data;""")
        self.db.commit()


    def start(self):
        self.drop_database()
        self.create_database()
        self.create_tables()
        self.load_csv()

#d = DB_Handler()
#d.start()
