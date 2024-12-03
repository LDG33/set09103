from flask import Flask, redirect, url_for, session, render_template, request
import sqlite3
app = Flask(__name__)

session['total']= 0

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
                    <input type="radio" name="quiz" value="answer1" id="answer1">attempt1</input><br>
                    <input type="radio" name="quiz" value="answer2" id="answer2">attempt2</input><br>
                    <input type="radio" name="quiz" value="answer3" id="answer3">attempt3</input><br>
                    <input type="radio" name="quiz" value="answer4" id="answer4">attempt4</input><br>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            <body></html>
        '''
        return page

    else:

            #print(str(POST['quiz']))
        answer = request.form['quiz']
        if(answer == "answer3"):
            try:
                if(session['total']):
                    session['total']+=1
                    return "Correct Answer"+session['total']
            except KeyError:
                pass
            return "Correct Answer "
        else:
            return answer+" is wrong answer"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


