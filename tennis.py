import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from collections import OrderedDict

import pymysql

from sqlalchemy import create_engine
import datetime
from database_files.db_connect import SQL_connect

from plotter import *


def total_win_loss_by_player(player_name):
    db = SQL_connect()
    db.execute('''USE tennis_data;''')

    player_name = str(player_name)

    sql_command_wins = """SELECT score, loser_name FROM atp_matches_1968_2017 \
                        WHERE winner_name = '%s';"""
    sql_command_loss = """SELECT score, winner_name FROM atp_matches_1968_2017 \
                        WHERE loser_name = '%s';"""

    wins = db.fetch(sql_command_wins %(player_name))
    total_wins = len(wins)

    loss = db.fetch(sql_command_loss %(player_name))
    total_loss = len(loss)

    df_wins = pd.DataFrame(list(wins), index=None, columns=['score', 'player'])
    df_loss = pd.DataFrame(list(loss), index=None, columns=['score', 'player'])

    df_wins.fillna(value=np.nan, inplace=True)
    df_loss.fillna(value=np.nan, inplace=True)




    dfs = [df_wins, df_loss]
    df_total_games = pd.concat(dfs)
    df_total_games.fillna(value=np.nan, inplace=True)
    total_games = total_loss + total_wins





def set_time_player(player_name):
    conn = SQL_connect()

    conn.execute('''USE tennis_data;''')

    sql_command_id_win = """SELECT score, best_of, minutes FROM atp_matches_1968_2017 WHERE winner_name = '%s';"""
    win_data = conn.fetch(sql_command_id_win %(player_name))

    sql_command_id_loss = """SELECT score, best_of, minutes FROM atp_matches_1968_2017 WHERE loser_name = '%s';"""
    loss_data = conn.fetch(sql_command_id_loss %(player_name))

    df_win = pd.DataFrame(list(win_data), index=None, columns=['score', 'best_of', 'time'])
    df_loss = pd.DataFrame(list(loss_data), index=None, columns=['score', 'best_of', 'time'])
    print (df_win)
    print (df_loss)



def player_rank(player_name):
    conn = SQL_connect()
    conn.execute('''USE tennis_data;''')

    first, last = player_name.split(' ')

    sql_command_id = """SELECT player_id FROM players WHERE first_name = '%s' AND last_name = '%s';"""
    player_id = conn.fetch(sql_command_id %(first, last))
    player_id = int(player_id[0][0])

    sql_command_rank = '''SELECT rank, ranking_date, ranking_points FROM player_rankings WHERE player_id = %d;'''
    rank = conn.fetch(sql_command_rank %(player_id))

    df = pd.DataFrame(list(rank), index=None, columns=['rank', 'ranking_date', 'ranking_points'])
    df = df.sort_values(by=['rank'], ascending=True)

    #Convert to date-time
    df['ranking_date'] = df['ranking_date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
    df['ranking_points'] = pd.to_numeric(df['ranking_points'], errors='ignore')

    df = df.reset_index(drop=True)
    df.fillna(value=np.nan, inplace=True)

    x_y_plot(df, 'ranking_date', 'rank', 'test1')
    x_y_plot(df, 'ranking_date', 'ranking_points', 'test2')
    x_y_plot(df, 'rank', 'ranking_points', 'test3')


#total_win_loss_by_player('Roger Federer')
player_rank('Roger Federer')
#set_time_player('Roger Federer')
