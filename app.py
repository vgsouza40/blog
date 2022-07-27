from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "Meu Primeiro Post",
        "body": "Aqui é o texto do post",
        "author": "Feulo",
        "created": datetime(2022,7,25)
    },
    {
        "title": "Meu Segundo Post",
        "body": "Aqui é o texto do post",
        "author": "Victor",
        "created": datetime(2022,7,26)
    },
    
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
