import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    init_db()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO visits DEFAULT VALUES;')
    conn.commit()
    cur.execute('SELECT count(id) FROM visits;')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>VZeta App</h1><p>Visitas registradas: {count}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
