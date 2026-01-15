from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )
    cursor = db.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
