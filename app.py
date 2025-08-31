from flask import Flask, render_template
import sqlite3

from create import create_blueprint
from read import read_blueprint
from update import update_blueprint
from delete import delete_blueprint

app = Flask(__name__)

app.register_blueprint(create_blueprint)
app.register_blueprint(read_blueprint)
app.register_blueprint(update_blueprint)
app.register_blueprint(delete_blueprint)

DB_FILE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def volunteer_list():
    conn = get_db_connection()
    volunteers = conn.execute("SELECT * FROM Volunteer").fetchall()
    conn.close()
    return render_template("index.html", volunteers=volunteers)

if __name__ == "__main__":
    app.run(debug=True)

