# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 23:38:37 2023

@author: Ryan Kugler
"""

from flask import Flask, render_template
import pandas
import fetchBoxScore

app = Flask(__name__)

@app.route('/')
def index():
    boxscores = fetchBoxScore.getBoxScores()
    return render_template('index.html', data=boxscores)

if __name__ == '__main__':
    app.run(debug=True)
