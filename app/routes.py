from app import app
from flask import render_template

@app.route('/')
@app.route('/index/<name>')
def index(name = "CeneoWebScraper \n" * 16):
    return render_template("index.html", text = name)


