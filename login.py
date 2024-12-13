from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3

app = Flask(__name__)
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
def root():
    if request.method == 'GET':
        login='''
            <!DOCTYPE html>
            <html><body>
                <form action="" method="POST" name="loginForm">
                    <input type="text" name="username" id="username"/>
                    <input type="password" name="password" id="password"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body></html>
        '''
        return login
    else:

        db = get_db()
        #db.cursor().execute('insert into albums values ("American Beauty", "Grateful Dead", "CD")')
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
            return usernameFromDB, passwordFromDB 



           
#return redirect(url_for('.login'))

"""
@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        user = request.form['email']
        pw = request.form['password']
        
        if check_auth(request.form['email'], request.form['password']):
            session['logged_in'] = True
            return redirect(url_for('.secret'))
    return render_template('login.html')
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



