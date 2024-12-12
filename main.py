from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from markupsafe import escape
from waitress import serve

con = sqlite3.connect('SWCG.db')

cur = con.cursor()

res = cur.execute('SELECT title FROM movie').fetchall()

print(res)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=res) #looks for the name of a file from the 'templates' file

# code inputs

@app.route('/gfg', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       print(first_name)
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+ first_name + last_name
    return render_template("input.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "POST":

        name = request.form.get('name')
        password = request.form.get('pword')
        con = sqlite3.connect('SWCG.db')
        cur = con.cursor()
        print(name)
        cur.execute("INSERT INTO user (name, password) VALUES(?, ?)", (name, password))
        con.commit()
        print(cur.execute(''' SELECT name FROM user ''').fetchall())
        return "Your account, with name " + name + " has been registered!"
    return render_template("register.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":

        name = request.form.get('name')
        password = request.form.get('pword')

        con = sqlite3.connect('SWCG.db')
        cur = con.cursor()

        res = cur.execute("SELECT name, password FROM user").fetchall()


        print(res)

        for i in range(0, len(res)):
            print(res[i][0])
            checkName = res[i][0]
            checkPassword = res[i][1]
            if checkName == name and checkPassword == password:
                return f"Account exists, with name {name}"
            else:
                return "YOU DOG"
    return render_template('login.html')







mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

