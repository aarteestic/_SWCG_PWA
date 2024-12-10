from flask import Flask, render_template, url_for

import sqlite3
from markupsafe import escape

from waitress import serve

con = sqlite3.connect('tutorial.db')

cur = con.cursor()

res = cur.execute('SELECT title FROM movie').fetchall()
print(res)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=res) #looks for the name of a file from the 'templates' file


mode = "prod"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000, threads = 2) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

