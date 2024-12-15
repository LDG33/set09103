from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3

app = Flask(__name__)

app.secret_key = 'qwertyuiop'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        registerVar='''
            <!DOCTYPE html>
            <html><body>
                <form action="" method="POST" name="registrationForm">
                    <input type="text" name="usernameReg" id="usernameReg"/>
                    <input type="password" name="passwordReg" id="passwordReg"/>
                    <input type="password" name="passwordReg2" id="passwordReg2"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body></html>
        '''
        return registerVar
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





