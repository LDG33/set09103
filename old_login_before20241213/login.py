from flask import Flask, redirect, url_for, session, render_template, request, g
import sqlite3
app = Flask(__name__)


DATABASE = 'var/quizapp.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        #db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST']) 
def login():       
    if request.method == 'GET':
        page='''
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
                <form action="" method="post" name="login_form">
                    <label for="question">Please provide your login:</label><br>
                    <input type="text" name="Login" id="login"/><br>
                    <label for="question">Please provide your password:</label><br>
                    <input type="password" name="Password" id="password"/><br>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            <body></html>
        '''
        return page

    else:
        login = request.form['Login']
        password = request.form['Password']
        
        page = []
        total = []
        
        db = get_db()
        cursor = db.cursor()
        #for row in cursor.execute("SELECT * FROM Users WHERE Login = 'Lu1'"):
        #cursor.execute("SELECT Password FROM Users WHERE Login=='"+login+"'")
        sql = ("SELECT * FROM Users WHERE Login="+login)
        cursor.execute(sql)
                       # WHERE Login = ?", (login) ///WHERE Login = 'Lu1'
        users = cursor.fetchall()
            #page.append(str(row))
        for user in users:
            total += user
        #puzniej condition zeby sprawdzic czy total nie jest puste
        return total[0]
        
        #return page
    
        cursor.execute("SELECT Password FROM Users")
                       # WHERE Login = ?", (login)
        password = cursor.fetchall()
        return str(*users[2])+"   "+str(*password[2])
        
    
        #return login+" "+password

        #Used to work - good for printing whole DB <-----------------------------------------
        #for row in db.cursor().execute("SELECT * FROM Users WHERE Name ='Lukasz' "):
            #return row
        #--------------------->
            
            #page.append(str(row))
        
        #for row in cursor.execute(sql):
            #print row

        #return login
        #return row[0]
        #return page
        





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


