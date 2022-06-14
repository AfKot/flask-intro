from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app_db1 = Flask(__name__)

app_db1.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app_db1)

app_db1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    app_db1.run(debug=True)