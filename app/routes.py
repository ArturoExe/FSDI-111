from flask import Flask

app=Flask(__name__)


@app.get("/aboutme")
def index():
    me={
        "first_name": "Arturo",
        "last_name":"Martinez",
        "hobbies":"Video Games",
        "active":True
    }

    return me #returns  json