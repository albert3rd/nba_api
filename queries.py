import psycopg2
import os 

connection_link = psycopg2.connect(os.getenv("DB_LINK"))

GET_ALL_PLAYERS = "SELCT * FROM nba_players"