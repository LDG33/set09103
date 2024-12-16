from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3

app = Flask(__name__)

app.secret_key = 'qwertyuiop123'
db_location = 'var/QuizAppDatabase.db'

@app.route("/")
def intro():
        return render_template('index.html')


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
            session['logged']=True
            return render_template('quiz.html', message='Correct You are logged in! ')
            #later redirect to quiz
            
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

        #Testing Validation -> If the entry already exist in DB (to not double register)
        '''    sqlReg = "SELECT * FROM Users WHERE Username = ?"
        cursor.execute(sqlReg, (userReg))

        entry = cursor.fetchone()
        if len(entry)>0:
            return render_template('register.html', messageReg='Sorry, User already exists!!!')
        '''
        #Testing Validation OLD
        '''
        #usernameFromDB_Reg = ""
        sqlReg = "SELECT * FROM Users WHERE Username = ?"
        cursor.execute(sqlReg, (userReg))

        rowsReg = cursor.fetchall()
        for rowReg in rowsReg:
            usernameFromDB_Reg = rowReg[1]

            if len(usernameFromDB_Reg)>0:
                return render_template('register.html', messageReg='Sorry, User already exists!!!')
        '''
        if(userReg=="")or(pw1=="")or(pw2==""):
            return render_template('register.html', messageReg='You have left empty fields')

        if(pw1==pw2):
            db.cursor().execute('INSERT INTO Users (Username, Password) VALUES (?, ?)',(userReg,pw2))
            db.commit()
            #no need for session? 
            return render_template('login.html', message='New account has been registerd')
        else:
            return render_template('register.html', messageReg='passwords do not match')

        
        
        #TEST IF ENTRY DOES NOT EXISTS IN DATABASE
        #Prohibit the empty submit

        sql = "SELECT * FROM Users WHERE Username = ? AND Password = ?"
        cursor.execute(sql, (user,pw))

        rows = cursor.fetchall()
        for row in rows:
            usernameFromDB = row[1]
            passwordFromDB = row[2]
            return usernameFromDB, passwordFromDB 
        
#-------------------Second Part: The QuizApp--------------------------------



@app.route("/quiz")
def hello():
    session['score']=0
    session['negative']=0
    session['q1']=0
    session['q2']=0
    session['q3']=0
    return render_template('quiz.html')

@app.route("/q1/")
def q1():
    return render_template('q1.html')

@app.route("/q1w/")
def q1w():
    session['negative']+=1
    session['q1']=0
    return render_template('q1w.html')

@app.route("/q1a/")
def q1a():
    session['score'] += 1
    session['q1']=1
    return render_template('q1a.html')

@app.route("/q2/")
def q2():
    return render_template('q2.html')

@app.route("/q2w/")
def q2w():
    session['negative']+=1
    session['q2']=0
    return render_template('q2w.html')

@app.route("/q2a/")
def q2a():
    session['score'] += 1
    session['q2']=1
    return render_template('q2a.html')

@app.route("/q3/")
def q3():
    return render_template('q3.html')

@app.route("/q3w/")
def q3w():
    session['negative']+=1
    session['q3']=0
    return render_template('q3w.html')

@app.route("/q3a/")
def q3a():
    session['score'] +=1
    session['q3']=1
    return render_template('q3a.html')

@app.route("/qsuccess/")
def qsuccess():
    #return render_template('qsuccess.html', score, negative,q1=session['q1'],q2=session['q2'],q3=session['q3'])
    return render_template('qsuccess.html', score=session['score'], negative=session['negative'],q1=session['q1'],q2=session['q2'],q3=session['q3'])

#-------------------Second Part: The QuizApp--------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)