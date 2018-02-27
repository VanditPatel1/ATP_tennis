import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from collections import OrderedDict

#FOR PYTHON 2
#import MySQLdb

#FOR PYTHON3
import pymysql

from sqlalchemy import create_engine
import datetime


def mySQL():
    conn = pymysql.connect(host='localhost',
                           user = 'root',
                           passwd = '12qwaszx',
                           port = 3306)
    
    return conn


def total_win_loss_by_player(player_name):
    conn = mySQL()
    curr = conn.cursor()
    curr.execute('''USE tennis_data;''')
    
    player_name = str(player_name)
    
    sql_command_wins = """SELECT score, loser_name FROM atp_matches_1968_2017 WHERE winner_name = '%s';"""
    sql_command_loss = """SELECT score, winner_name FROM atp_matches_1968_2017 WHERE loser_name = '%s';"""
    
    curr.execute(sql_command_wins %(player_name))
    wins = curr.fetchall()
    total_wins = len(wins)
    
    curr.execute(sql_command_loss %(player_name))
    loss = curr.fetchall()
    total_loss = len(loss)
    
    df_wins = pd.DataFrame(list(wins), index=None, columns=['score', 'player'])
    df_loss = pd.DataFrame(list(loss), index=None, columns=['score', 'player'])
    
    dfs = [df_wins, df_loss]
    
    df_total_games = pd.concat(dfs)
    total_games = total_loss + total_wins
    
    print (df_wins)
    print (df_loss)
    print (df_total_games)
    
  
    
def set_time_player(player_name):
    conn = mySQL()
    curr = conn.cursor()
    curr.execute('''USE tennis_data;''')
    
    player_name = str(player_name)
    
    sql_command_id_win = """SELECT score, best_of, minutes FROM atp_matches_1968_2017 WHERE winner_name = '%s';"""
    curr.execute(sql_command_id_win %(player_name))
    win_data = curr.fetchall()
    
    sql_command_id_loss = """SELECT score, best_of, minutes FROM atp_matches_1968_2017 WHERE loser_name = '%s';"""
    curr.execute(sql_command_id_loss %(player_name))
    loss_data = curr.fetchall()
    
    df_win = pd.DataFrame(list(win_data), index=None, columns=['score', 'best_of', 'time'])
    df_loss = pd.DataFrame(list(loss_data), index=None, columns=['score', 'best_of', 'time'])
    print (df_win)
    print (df_loss)
    
    
    
def player_rank(player_name):
    conn = mySQL()
    curr = conn.cursor()
    curr.execute('''USE tennis_data;''')
    
    first, last = player_name.split(' ')
    
    sql_command_id = """SELECT player_id FROM players WHERE first_name = '%s' AND last_name = '%s';"""
    curr.execute(sql_command_id %(first, last))
    player_id = curr.fetchall()
    player_id = int(player_id[0][0])
    
    sql_command_rank = '''SELECT rank, ranking_date, ranking_points FROM player_rankings WHERE player_id = %d;'''
    curr.execute(sql_command_rank %(player_id))
    rank = curr.fetchall()
        
    df = pd.DataFrame(list(rank), index=None, columns=['rank', 'ranking_date', 'ranking_points'])
    df = df.sort_values(by=['rank'], ascending=True)
    
    #Convert to date-time
    df['ranking_date'] = df['ranking_date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
    df = df.reset_index(drop=True)
    print (df)
    
    df.plot(x='ranking_date', y='rank')
    df.plot(x='ranking_date', y='ranking_points')
    df.plot(x='rank', y='ranking_points')
    
        
#total_win_loss_by_player('Roger Federer')
#player_rank('Roger Federer')
set_time_player('Roger Federer')