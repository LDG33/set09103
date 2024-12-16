from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3
#import login

app = Flask(__name__)

app.secret_key = 'qwertyuiop'


@app.route("/")
def intro():
        return render_template('index.html')

db_location = 'var/QuizAppDatabase.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route("/login", methods=['GET', 'POST'])
def login():

    usernameFromDB=""
    passwordFromDB=""

    if request.method == 'GET':
        return render_template('login.html')
    else:

        db = get_db()
        #db.commit()
        cursor=db.cursor()

        user = request.form['username']
        pw = request.form['password']

        sql = "SELECT * FROM Users WHERE Username = ? AND Password = ?"
        cursor.execute(sql, (user,pw))

        rows = cursor.fetchall()
        for row in rows:
            usernameFromDB = row[1]
            passwordFromDB = row[2]

        if (user == "")or(pw == ""):
            #session['emptyInput']
            return render_template('login.html', message='Sorry No Input, Type Again: ')
        elif (usernameFromDB == user)or(passwordFromDB == pw):
            return render_template('login.html', message='Correct You are logged in! ')
            #later redirect to quiz
            #set the session
        else:
            return render_template('login.html', message='Sorry wrong credentials')
            """
            if(usernameFromDB == user)and(passwordFromDB == pw):
                session['logged']=True
                return "true"
                #return render_template('/quiz')
            else:
                session['logged']=False
                return "false"
                #it cannot be like that because it will reset the session
            """

            #if (usernameFromDB != None):
                #return redirect(url_for('.register'))
        #return register() 

#redirect register to login 
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        db = get_db()
        cursor=db.cursor()

        userReg = request.form['usernameReg']
        pw1 = request.form['passwordReg']
        pw2 = request.form['passwordReg2']




        if(pw1==pw2):
            db.cursor().execute('INSERT INTO Users (Username, Password) VALUES (?, ?)',(userReg,pw2))
            db.commit()
        else:
            return "passwords do not match"

        return "happy clam"
        
        #TEST IF ENTRY DOES NOT EXISTS IN DATABASE

        sql = "SELECT * FROM Users WHERE Username = ? AND Password = ?"
        cursor.execute(sql, (user,pw))

        rows = cursor.fetchall()
        for row in rows:
            usernameFromDB = row[1]
            passwordFromDB = row[2]
            return usernameFromDB, passwordFromDB 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)