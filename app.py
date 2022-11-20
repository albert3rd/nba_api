from flask import Flask
from dotenv import load_dotenv
import psycopg2
import os 
import queries

load_dotenv()

app = Flask(__name__)

db_user=os.getenv('USER')
db_password=os.getenv('DB_PASSWORD')
connection_link = psycopg2.connect(database='nba_api', user=db_user, password=db_password, host='127.0.0.1', port='5432')
cursor = connection_link.cursor()

fetch_one = cursor.fetchone()
fetch_all = cursor.fetchall()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"