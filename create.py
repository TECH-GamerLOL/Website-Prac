from flask import Blueprint, render_template, request, redirect
import sqlite3

create_blueprint = Blueprint('create', __name__)
DB_FILE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@create_blueprint.route("/volunteer/new", methods=["GET", "POST"])
def create_volunteer():
    conn = get_db_connection()
    organisations = conn.execute("SELECT * FROM Organisation").fetchall()
    conn.close()
    
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        phoneNumber = request.form["phoneNumber"]
        availability = request.form["availability"]
        location = request.form["location"]
        joinDate = request.form["joinDate"]
        organisationID = request.form["organisationID"]
        
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO Volunteer (firstName, lastName, email, phoneNumber, availability, location, joinDate, organisationID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (firstName, lastName, email, phoneNumber, availability, location, joinDate, organisationID)
        )
        conn.commit()
        conn.close()
        return redirect("/")
    
    return render_template("create_volunteer.html", organisations=organisations)
