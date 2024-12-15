from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3
import login

app = Flask(__name__)

app.secret_key = 'qwertyuiop9'

#print("Hello World!")

#I AM TESTING THIS FOR NOW -> THE GOAL IS TO MAKE A SMOOTH/CONSISTENT NAVIGATION - LDG 20241215

@app.route("/")
def intro():
        
        #link = redirect(url_for('.root'))

        page='''
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
                <h1>Welcome to QuizApp</h1>
                <p>To start playing quizzes you need to log in first</p>
                <p>Please LogIn here: <a href="'''+login.login()+'''">Login Page</a></p>
            <body></html>
        '''
        return page

                    #redirect(url_for('.index'))

        #{{redirect(url_for('.root'))}}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)