from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from markupsafe import escape
from waitress import serve
login = False
sessionUsername = ''
con = sqlite3.connect('SWCG.db')
cur = con.cursor()


movieUser = cur.execute('SELECT * FROM user').fetchall()

movieRecord = cur.execute('SELECT * FROM movie').fetchall()

movieID = cur.execute(''' SELECT id FROM movie ''').fetchall()
# movieRecord is a list of all movies and their data
# movieRecord[i] returns the list of one movie, containing its name, year of publication, rating out of 10, and genre
# respectively
movieReview = cur.execute('SELECT * FROM reviews').fetchall()

movieUsername = cur.execute('SELECT name FROM user').fetchall()

cur.close()
con.close()


app = Flask(__name__)


@app.route("/") #To home page
def index():
    return render_template("index.html", movie=movieRecord, login=login, sessionUsername=sessionUsername) #looks for the name of a file from the 'templates' file

# code inputs

@app.route("/movies")  #To movies page
def movies():
    if login:
        print(login)
        print(f'User {sessionUsername} is in the movies page!')
    return render_template("movies.html", movie=movieRecord, movieID=movieID, login=login, sessionUsername=sessionUsername)

@app.route("/users")
def users():
    return render_template("users.html", movieUsername=movieUsername, movieReview=movieReview, movieID=movieID, login=login, sessionUsername=sessionUsername)


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

@app.route('/login', methods = ['GET', 'POST']) #To login page
def login_1():
        if request.method == "POST": #for logging into an account, once form is sent

            name = request.form.get('name')
            password = request.form.get('pword')


            con = sqlite3.connect('SWCG.db')
            cur = con.cursor()

            movieRecord = cur.execute("SELECT name, password FROM user").fetchall()
            cur.close()
            con.close()

            print(movieRecord)
            exists = False
            for i in range(0, len(movieRecord)):
                print(movieRecord[i][0])
                checkName = movieRecord[i][0]
                checkPassword = movieRecord[i][1]
                if checkName == name and checkPassword == password: #if name and password runs, then account exists
                    global sessionUsername
                    sessionUsername = checkName #gets sessionUsername
                    exists = True
            if exists == True:
                global login
                login = True # user is now logged in, allowing pages to have their logged in version
                return f"Account exists, with name {name}"
                
            else:
                return "You DOG."
        return render_template('login1.html')

@app.route('/users/<string:name>')
def user(name):
    userReview = []
    for review in movieReview:
        if review[2] == name:
            userReview.append(review)
    for i in range(0, len(movieUser)):
        print(movieUser[i][0])
        if name == movieUser[i][0]:
            return render_template('user.html', userReview=userReview, login=login, sessionUsername=sessionUsername, name=name)
        else:
            next
    return 'Error! User not found!' #replace with error page

#Dynamically creates movie pages for each movie in the SWCG database.
@app.route('/movies/<int:movieNumber>') #To each specific movie
def movie(movieNumber): #movieNumber not to be confused with movieID, which is for the SWCG database (;
    for i in range(0, len(movieID)): #stops indexing at j-1 because python is dumb!!!
        print(i)
        if movieNumber == movieID[i][0] - 1: #to begin indexing from 0
            return render_template('review.html', movieNumber=movieNumber, movie=movieRecord, movieReview=movieReview, login=login, sessionUsername=sessionUsername)
        else:
            next
    return 'Error! Movie not found!' #replace with error page






mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        serve(app, host="0.0.0.0", port=8000) #mock production server

    elif mode =="dev":
        app.run(host="0.0.0.0", debug=True)

