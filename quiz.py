from flask import Flask, redirect, url_for, session, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def start():
    if request.method == 'GET':
        page='''
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
                <form action="" method="post" name="form">
                    <label for="question">Question:</label><br>
                    <input type="radio" naem="quiz" value="answer1"><br>
                    <input type="radio" name="quiz" value="answer2"><br>
                    <input type="radio" name="quiz" value="answer3"><br>
                    <input type="radio" name="quiz" value="answer4"><br>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            <body></html>
        '''
        return page
    else:
        #print(str(POST['quiz']))
        answer = request.form['quiz']
        print(answer)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


