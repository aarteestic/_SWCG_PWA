from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from markupsafe import escape
from waitress import serve

con = sqlite3.connect('SWCG.db')
cur = con.cursor()

res = cur.execute('SELECT * FROM movie').fetchall()
# res is a list of all movies and their data
# res[i] returns the list of one movie, containing its name, year of publication, rating out of 10, and genre
# respectively

# rowid is obtained another way (see res2) 

# currently redundant database code
app = Flask(__name__)


@app.route("/") #To home page
def index():
    return render_template("index.html", movie=res) #looks for the name of a file from the 'templates' file

# code inputs

@app.route("/movies")  #To movies page
def movies():
    return render_template("movies.html", movie=res)

@app.route("/register", methods = ['GET', 'POST']) #for registering an account
def register():
    if request.method == "POST":
        #Handles account registration into the SWCG user table
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

@app.route('/login_1', methods = ['GET', 'POST']) #To login page
def login_1():
        if request.method == "POST": #for logging into an account, once form is sent

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
                userInfo = name # sets a name, currently nonfunctional
                return f"Account exists, with name {name}"
                
            else:
                return "You DOG."
        return render_template('login1.html')



res2 = cur.execute(''' SELECT rowid FROM movie''').fetchall()
#Dynamically created movie pages for each movie in the SWCG database.
@app.route((f'/movies/<int:movieID>')) #To each specific movie
def movie(movieID):
    for i in range(0, len(res2)):
        if movieID == res2[i][0]:
            return render_template('review.html', movieID=movieID)
        else:
            return 'Error! Movie not found.' #need error page.






mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

