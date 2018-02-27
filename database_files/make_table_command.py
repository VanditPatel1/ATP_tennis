atp_matches_1968_2017 = """
atp_matches_1968_2017 ( 
tourney_id VARCHAR(40), 
tourney_name CHAR(20), 
surface CHAR(10), 
draw_size INT,
tourney_level CHAR(5),
tourney_date VARCHAR(10),
match_num INT, 
winner_id INT,
winner_seed INT,
winner_entry VARCHAR(5),
winner_name CHAR(30),
winner_hand CHAR(2),
winner_ht FLOAT(4),
winner_ioc CHAR(10),
winner_age FLOAT(5),
winner_rank INT,
winner_rank_points FLOAT(2),
loser_id INT,
loser_seed INT,
loser_entry VARCHAR(5),
loser_name CHAR(30),
loser_hand CHAR(2),
loser_ht FLOAT(4),
loser_ioc CHAR(10),
loser_age FLOAT(5),
loser_rank INT,
loser_rank_points FLOAT(2), 
score VARCHAR(25),
best_of INT,
round VARCHAR(5),
minutes FLOAT(5),
w_ace VARCHAR(5),
w_df VARCHAR(5),
w_svpt VARCHAR(5),
w_1stIn VARCHAR(5),
w_1stWon VARCHAR(5),
w_2ndWon VARCHAR(5),
w_SvGms VARCHAR(5),
w_bpSaved VARCHAR(5),
w_bpFaced VARCHAR(5),
l_ace VARCHAR(5),
l_df VARCHAR(5),
l_svpt VARCHAR(5),
l_1stIn VARCHAR(5),
l_1stWon VARCHAR(5),
l_2ndWon VARCHAR(5),
l_SvGms VARCHAR(5),
l_bpSaved VARCHAR(5),
l_bpFaced VARCHAR(5));
"""


player_rankings = """
player_rankings (
ranking_date VARCHAR(10),
rank INT,
player_id INT,
ranking_points INT);
"""

players = """
players (
player_id INT,
first_name CHAR(15),
last_name CHAR(15),
hand CHAR(3),
birth_date VARCHAR(10),
country_code CHAR(5));
"""

players_header = ['player_id', 'first_name', 'last_name', 'hand', 'birth_date', 'country_code']

players_rankings_header = ['ranking_date', 'rank', 'player_id', 'ranking_points']