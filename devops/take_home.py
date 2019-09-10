'''
This application won't work! Your challenge is to fix that.

Please connect this application to a persistent database
and encapsulate it in such a way that you can send us a 
zip of the dir and we can have this up and running if we have
the following dependencies installed:

* Docker
* Python
* Flask
* SqlAlchemy

How you do so is entirely up to you. 

HINT: Here at LeafLink we use docker-compose to manage our services 

Deliverable: a zip or otherwise compressed file. This file
MUST include take_home.py and it MUST include a README.MD
that will explain how to run this app so it works. 

HINT: The less we need to type to see that it works, the better :)
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  "localhost maybe? up to you!"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return "It works"

db.create_all()
app.run()
