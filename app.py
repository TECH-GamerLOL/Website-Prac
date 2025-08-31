from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_volunteers():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  
    cur = conn.cursor()
    cur.execute("SELECT firstName, lastName, email FROM Volunteer")
    rows = cur.fetchall()
    conn.close()
    return rows

@app.route("/")
def volunteer_list():
    volunteers = get_volunteers()
    print("Fetched volunteers:", volunteers)
    return render_template("index.html", volunteers=volunteers)

if __name__ == "__main__":
    app.run(debug=True)
