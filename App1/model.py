from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app = Flask(__name__)
db = SQLAlchemy(app)
DATABASE = 'ExpenseManagement'
PASSWORD = 'password123'
USER = 'root'
HOSTNAME = 'dbinstance1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def createDB():
    engine = sqlalchemy.create_engine('mysql://%s:%s@%s' % (USER, PASSWORD, HOSTNAME))
    engine.execute("CREATE DATABASE IF NOT EXISTS %s" % (DATABASE))

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=False)
    category = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(100), unique=False)
    link = db.Column(db.String(100), unique=False)
    estimated_costs = db.Column(db.String(100), unique=False)
    submit_date = db.Column(db.String(100), unique=False)
    status = db.Column(db.String(100), unique=False)
    decision_date = db.Column(db.String(100), unique=False)

    def __init__(self,id, name, email, category, description, link, estimated_costs, submit_date, status, decision_date):
        self.id=id
        self.name = name
        self.email = email
        self.category = category
        self.description = description
        self.link = link
        self.estimated_costs = estimated_costs
        self.submit_date = submit_date
        self.status = status
        self.decision_date = decision_date
