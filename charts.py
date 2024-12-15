import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, g, request, redirect, render_template, session, url_for
import sqlite3

app = Flask(__name__)

#print("Hello World!")


@app.route("/")
def root():
    plt.plot([5],[7], 'ro')

    return plt.show()



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)