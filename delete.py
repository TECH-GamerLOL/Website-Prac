from flask import Blueprint, redirect
import sqlite3

delete_blueprint = Blueprint('delete', __name__)
DB_FILE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@delete_blueprint.route("/event/delete/<int:id>", methods=["POST"])
def delete_event(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM Event WHERE eventID = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/events")
