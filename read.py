from flask import Blueprint, render_template
import sqlite3

read_blueprint = Blueprint('read', __name__)
DB_FILE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@read_blueprint.route("/organisations")
def list_organisations():
    conn = get_db_connection()
    organisations = conn.execute("SELECT * FROM Organisation").fetchall()
    conn.close()
    return render_template("organisations.html", organisations=organisations)

@read_blueprint.route("/events")
def list_events():
    conn = get_db_connection()
    events = conn.execute("SELECT * FROM Event").fetchall()
    conn.close()
    return render_template("events.html", events=events)
