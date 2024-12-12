from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from markupsafe import escape
from waitress import serve

con = sqlite3.connect('SWCG.db')
cur = con.cursor()
res = cur.execute('SELECT title FROM movie').fetchall()
# currently redundant database code
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movie=res) #looks for the name of a file from the 'templates' file

# code inputs

@app.route("/movies")
def movies():
    return render_template("movies.html")

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
        cur.close()
        return "Your account, with name " + name + " has been registered!"
    return render_template("register.html")

@app.route('/login_1', methods = ['GET', 'POST']) #production login
def login_1():
        if request.method == "POST": #if INFORMATION is sent, this code runs

            name = request.form.get('name')
            password = request.form.get('pword')


            con = sqlite3.connect('SWCG.db')
            cur = con.cursor()

            res = cur.execute("SELECT name, password FROM user").fetchall()
            cur.close()
            
            print(res)
            exists = False
            for i in range(0, len(res)):
                print(res[i][0])
                checkName = res[i][0]
                checkPassword = res[i][1]
                if checkName == name and checkPassword == password: #if name and password runs, then account exists
                    exists = True
            if exists == True:
                return f"Account exists, with name {name}"
            else:
                return "You DOG."
        return render_template('login1.html')








mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

