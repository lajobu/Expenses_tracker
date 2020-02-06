from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses_tracker.db'
db = SQLAlchemy(app)

#Database:

#1)Table User:


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    first_name = db.Column(db.String(15), nullable=False)
    second_name = db.Column(db.String(25), nullable=True, default='N/A')
    email = db.Column(db.String(50), nullable=False)
    user_city = db.Column(db.String(15), nullable=True, default='N/A')
    prof_status = db.Column(db.String(15), nullable=True, default='N/A')
    password = db.Column(db.String(100), nullable=False)
    outcomes = db.relationship('Outcome', backref='categories', lazy=True)
    incomes = db.relationship('Income', backref='categories1', lazy=True)

    def __init__(self, username, first_name, second_name, email, user_city, prof_status, password):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.user_city = user_city
        self.prof_status = prof_status
        self.password = password

#2)Table Category:


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(15), nullable=False)
    outcomes1 = db.relationship('Outcome', backref='categories2', lazy=True)
    incomes1 = db.relationship('Income', backref='categories3', lazy=True)

    def __init__(self, category_name):
        self.category_name = category_name

#3)Table Sender:


class Sender(db.Model):
    __tablename__ = 'sender'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_name = db.Column(db.String(15), nullable=False)
    sender_city = db.Column(db.String(15), nullable=True, default='N/A')
    sender_country = db.Column(db.String(15), nullable=True, default='N/A')
    senders = db.relationship('Income', backref='senders', lazy=True)

    def __init__(self, sender_name, sender_city, sender_country):
        self.sender_name = sender_name
        self.sender_city = sender_city
        self.sender_country = sender_country

#4)Table Vendor:


class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor_name = db.Column(db.String(15), nullable=False)
    vendor_city = db.Column(db.String(15), nullable=True, default='N/A')
    vendor_country = db.Column(db.String(15), nullable=True, default='N/A')
    vendors = db.relationship('Outcome', backref='vendors', lazy=True)

    def __init__(self, vendor_name, vendor_city, vendor_country):
        self.vendor_name = vendor_name
        self.vendor_city = vendor_city
        self.vendor_country = vendor_country

#5)Table Outcome:


class Outcome(db.Model):
    __tablename__ = 'outcome'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_vendor = db.Column(db.Integer, db.ForeignKey('vendor.id'),
                          nullable=False)
    ID_user = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    ID_category = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    amount_outcome = db.Column(db.DECIMAL(10, 2), nullable=False)
    currency_outcome = db.Column(db.String(3), nullable=False)
    date_outcome = db.Column(db.String(15), nullable=False)
    date_outcome1 = db.Column(db.Integer, nullable=False)
    p_m_outcome = db.Column(db.String(20), nullable=False)
    comment_outcome = db.Column(db.String(255), nullable=True, default='N/A')

    def __init__(self, ID_vendor, ID_user, ID_category, amount_outcome, currency_outcome, date_outcome, p_m_outcome, comment_outcome, date_outcome1):
        self.ID_vendor = ID_vendor
        self.ID_user = ID_user
        self.ID_category = ID_category
        self.amount_outcome = amount_outcome
        self.currency_outcome = currency_outcome
        self.date_outcome = date_outcome
        self.date_outcome1 = date_outcome1
        self.p_m_outcome = p_m_outcome
        self.comment_outcome = comment_outcome

#6)Table Income:


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_sender = db.Column(db.Integer, db.ForeignKey('sender.id'),
                          nullable=False)
    ID_user = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    ID_category = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    amount_income = db.Column(db.DECIMAL(10, 2), nullable=False)
    currency_income = db.Column(db.String(3), nullable=False)
    date_income = db.Column(db.String(15), nullable=False)
    date_income1 = db.Column(db.Integer, nullable=False)
    p_m_income = db.Column(db.String(15), nullable=False)
    comment_income = db.Column(db.String(255), nullable=True, default='N/A')

    def __init__(self, ID_sender, ID_user, ID_category, amount_income, currency_income, date_income, p_m_income, comment_income, date_income1):
        self.ID_sender = ID_sender
        self.ID_user = ID_user
        self.ID_category = ID_category
        self.amount_income = amount_income
        self.currency_income = currency_income
        self.date_income = date_income
        self.date_income1 = date_income1
        self.p_m_income = p_m_income
        self.comment_income = comment_income


#After the tables are created:

#a)First run the below code in python terminal, in order to create the file: expenses_tracker.db

#from app import db
#db.create_all()

#b)Run the script create_values.py, in order to populate the database with the main data

#c)We can confirm that the tables were created from the terminal:_

#sqlite3 expenses_tracker.db
#.tables - We should obtain all the tables created

#It is posible to check that all is fine opening the .db file in sqlite

#After the tables are created:

#a)First run the below code in python terminal, in order to create the file: expenses_tracker.db

#from app import db
#db.create_all()

#b)Run the script create_values.py, in order to populate the database with the main data

#c)We can confirm that the tables were created from the terminal:_

#sqlite3 expenses_tracker.db
#.tables - We should obtain all the tables created

#It is posible to check that all is fine opening the .db file in sqlite


if __name__ == "__main__":
    # Like that we do not need to restart the server every time
    app.run(debug=True)
