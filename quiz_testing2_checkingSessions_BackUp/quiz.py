from flask import Flask, render_template, session
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def hello():
    session['score']= 0
    return render_template('index.html')

@app.route("/q1/")
def q1():
    return render_template('q1.html')

@app.route("/q1w/")
def q1w():
    return render_template('q1w.html')

@app.route("/q1a/")
def q1a():
    session['score'] += 1
    return render_template('q1a.html')

@app.route("/q2/")
def q2():
    return render_template('q2.html')

@app.route("/q2w/")
def q2w():
    return render_template('q2w.html')

@app.route("/q2a/")
def q2a():
    session['score'] += 1
    return render_template('q2a.html')

@app.route("/q3/")
def q3():
    return render_template('q3.html')

@app.route("/q3w/")
def q3w():
    return render_template('q3w.html')

@app.route("/q3a/")
def q3a():
    session['score'] += 1
    return render_template('q3a.html')

@app.route("/success/")
def success():
    return render_template('success.html', score=session['score'])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")