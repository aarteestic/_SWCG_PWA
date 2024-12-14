from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from markupsafe import escape
from waitress import serve

con = sqlite3.connect('SWCG.db')
cur = con.cursor()

movieRecord = cur.execute('SELECT * FROM movie').fetchall()

movieID = cur.execute(''' SELECT id FROM movie ''').fetchall()
# movieRecord is a list of all movies and their data
# movieRecord[i] returns the list of one movie, containing its name, year of publication, rating out of 10, and genre
# respectively
movieReview = cur.execute('SELECT * FROM reviews').fetchall()


app = Flask(__name__)


@app.route("/") #To home page
def index():
    return render_template("index.html", movie=movieRecord) #looks for the name of a file from the 'templates' file

# code inputs

@app.route("/movies")  #To movies page
def movies():
    return render_template("movies.html", movie=movieRecord, movieID=movieID)

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

            movieRecord = cur.execute("SELECT name, password FROM user").fetchall()
            cur.close()
            
            print(movieRecord)
            exists = False
            for i in range(0, len(movieRecord)):
                print(movieRecord[i][0])
                checkName = movieRecord[i][0]
                checkPassword = movieRecord[i][1]
                if checkName == name and checkPassword == password: #if name and password runs, then account exists
                    exists = True
            if exists == True:
                userInfo = name # sets a name, currently nonfunctional
                return f"Account exists, with name {name}"
                
            else:
                return "You DOG."
        return render_template('login1.html')



#Dynamically creates movie pages for each movie in the SWCG database.
@app.route((f'/movies/<int:movieNumber>')) #To each specific movie
def movie(movieNumber): #movieNumber not to be confused with movieID, which is for the SWCG database (;
    for i in range(0, len(movieID)): #stops indexing at j-1 because python is dumb!!!
        print(i)
        if movieNumber == movieID[i][0] - 1: #to begin indexing from 0
            return render_template('review.html', movieNumber=movieNumber, movie=movieRecord, movieReview=movieReview)
        else:
            next
    return 'Error! Movie not found!'






mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

