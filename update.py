from flask import Blueprint, render_template, request, redirect
import sqlite3

update_blueprint = Blueprint('update', __name__)
DB_FILE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@update_blueprint.route("/volunteer/update/<int:id>", methods=["GET", "POST"])
def update_volunteer(id):
    conn = get_db_connection()
    volunteer = conn.execute("SELECT * FROM Volunteer WHERE volunteerID = ?", (id,)).fetchone()
    
    if request.method == "POST":
        new_phone = request.form["phoneNumber"]
        conn.execute("UPDATE Volunteer SET phoneNumber = ? WHERE volunteerID = ?", (new_phone, id))
        conn.commit()
        conn.close()
        return redirect("/")
    
    conn.close()
    return render_template("update_volunteer.html", volunteer=volunteer)
