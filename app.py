from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

db.init_app(app)


@app.route("/")
def home():
    return "My flask app"


if __name__ == "__main__":
    app.run(debug=True,port=5000)