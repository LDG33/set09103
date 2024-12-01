from flask import Flask, redirect, url_for, session, render_template
import sqlite3
app = Flask(__name__)

@app.route('/') 
def start():
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
                    <input type="text" name="Password" id="password"/><br>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            <body></html>
        '''
        return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


