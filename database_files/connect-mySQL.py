import MySQLdb
from make_table_command import *
import pandas as pd
import os
from sqlalchemy import create_engine

def mySQL():
    conn = MySQLdb.connect (host='localhost',
                            user = 'root',
                            passwd = '12qwaszx')
    return conn


def create_database():
    conn = mySQL()
    curr = conn.cursor()
    create_tennis_database = """CREATE DATABASE tennis_data;"""
    curr.execute(create_tennis_database)
    conn.commit()
    conn.close()


def create_tables():
    conn = mySQL()
    curr = conn.cursor()
    curr.execute("""USE tennis_data;""")
    sql_command = """CREATE TABLE %s""" 
    tennis_matches_tables = sql_command % (atp_matches_1968_2017)
    players_table = sql_command % (players)
    player_ranking_table = sql_command % (player_rankings)
    curr.execute(tennis_matches_tables)
    curr.execute(players_table)
    curr.execute(player_ranking_table)
    conn.commit()
    conn.close()

def get_file_list():
       
    l = os.listdir(os.path.abspath('../tennis_atp'))
    return l

def what_table(f):
        if 'atp_matches' in f:
            return 'atp_matches_1968_2017'
            
        elif 'atp_ranking' in f:
            return 'player_rankings'
            
        elif 'atp_player' in f:
            return 'players'
            
        else:
            print ('Dont need this file')
            return None
    

def load_csv():
    #curr = conn.cursor()
    #curr.execute("""USE tennis_data;""")
    
    engine = create_engine('mysql+mysqldb://root:12qwaszx@localhost/tennis_data')
    path = os.path.abspath('../tennis_atp') + '/'
    files = get_file_list()
    
    for f in files:
        table = what_table(f)
        if table:
            if table is not 'atp_matches_1968_2017':
                df = add_headers(f, table)
                print (table)
                print (df) 
                df.to_sql(con=engine, name=table, index=False, if_exists='append')
                
            else: 
                df = pd.read_csv(path+f)
                df.to_sql(con=engine, name=table, index=False, if_exists='append')


    
    #df.to_sql(con=con, name='table_name_for_df', if_exists='replace', flavor='mysql')
    
def add_headers(f, table):
 
    path = os.path.abspath('../tennis_atp') + '/'
    if 'player_ranking' in table:
        df = pd.read_csv(path+f, names=players_rankings_header)
        return df
    
    elif 'players' in table:
        df = pd.read_csv(path+f, names=players_header)
        return df
                
    else:
        print ('none')
    
    
def drop_database():
    conn = mySQL()
    curr = conn.cursor()
    curr.execute("""DROP database tennis_data;""")
    conn.commit()
    conn.close()


def start():
    drop_database()
    create_database()
    create_tables()
    load_csv()

