from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import g
import sqlite3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp

import io
import base64
import urllib

connection = sqlite3.connect('expenses_tracker.db', check_same_thread=False)
DATABASE = './expenses_tracker.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'developmentkey'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Database:

# 1)Table User:


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

# 2)Table Category:


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(15), nullable=False)
    outcomes1 = db.relationship('Outcome', backref='categories2', lazy=True)
    incomes1 = db.relationship('Income', backref='categories3', lazy=True)

    def __init__(self, category_name):
        self.category_name = category_name

# 3)Table Sender:


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

# 4)Table Vendor:


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

# 5)Table Outcome:


class Outcome(db.Model):
    __tablename__ = 'outcome'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_user = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    ID_vendor = db.Column(db.Integer, db.ForeignKey('vendor.id'),
                          nullable=False)
    ID_category = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    amount_outcome = db.Column(db.DECIMAL(10, 2), nullable=False)
    currency_outcome = db.Column(db.String(3), nullable=False)
    date_outcome = db.Column(db.String(15), nullable=False)
    date_outcome1 = db.Column(db.Integer, nullable=False)
    p_m_outcome = db.Column(db.String(20), nullable=False)
    comment_outcome = db.Column(db.String(255), nullable=True, default='N/A')

    def __init__(self, ID_user, ID_vendor, ID_category, amount_outcome,
                 currency_outcome, date_outcome, p_m_outcome, comment_outcome, date_outcome1):
        self.ID_user = ID_user
        self.ID_vendor = ID_vendor
        self.ID_category = ID_category
        self.amount_outcome = amount_outcome
        self.currency_outcome = currency_outcome
        self.date_outcome = date_outcome
        self.date_outcome1 = date_outcome1
        self.p_m_outcome = p_m_outcome
        self.comment_outcome = comment_outcome

# 6)Table Income:


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_user = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    ID_sender = db.Column(db.Integer, db.ForeignKey('sender.id'),
                          nullable=False)
    ID_category = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    amount_income = db.Column(db.DECIMAL(10, 2), nullable=False)
    currency_income = db.Column(db.String(3), nullable=False)
    date_income = db.Column(db.String(15), nullable=False)
    date_income1 = db.Column(db.Integer, nullable=False)
    p_m_income = db.Column(db.String(15), nullable=False)
    comment_income = db.Column(db.String(255), nullable=True, default='N/A')

    def __init__(self, ID_user, ID_sender, ID_category, amount_income,
                 currency_income, date_income, p_m_income, comment_income, date_income1):
        self.ID_user = ID_user
        self.ID_sender = ID_sender
        self.ID_category = ID_category
        self.amount_income = amount_income
        self.currency_income = currency_income
        self.date_income = date_income
        self.date_income1 = date_income1
        self.p_m_income = p_m_income
        self.comment_income = comment_income

# After the tables are created:

# a)First run the below code in python terminal, in order to create the file: expenses_tracker.db

#from app import db
# db.create_all()

# b)Run the script create_values.py, in order to populate the database with the main data

# c)We can confirm that the tables were created from the terminal:_

# sqlite3 expenses_tracker.db
# .tables - We should obtain all the tables created

# It is posible to check that all is fine opening the .db file in sqlite

# HTML+CSS:

# 1)Login page:


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def valid_login(username, password):
    user = query_db('select * from User where username = ? and password = ?',
                    [username, password], one=True)
    if user is None:
        return False
    else:
        return True


def log_the_user_in(username):
    return render_template('index.html', username=username)


@app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route("/logout.html")
def logout():
    return render_template('login.html')

# 2)Index page:


@app.route('/index.html')
def index1():
    return render_template('index.html')

# 3)Data form income page:


@app.route('/data_form_income.html', methods=['GET', 'POST'])
def data_form_income():

    if request.method == 'POST':
        newID_user = request.form['ID_user']
        newID_sender = request.form['ID_sender']
        newID_category = request.form['ID_category']
        newamount_income = request.form['amount_income']
        newcurrency_income = request.form['currency_income']
        newdate_income = request.form['date_income']
        newdate_income1 = request.form['date_income1']
        newp_m_income = request.form['p_m_income']
        newcomment_income = request.form['comment_income']
        newIncome = Income(newID_user, newID_sender, newID_category, newamount_income,
                           newcurrency_income, newdate_income, newp_m_income, newcomment_income, newdate_income1)
        db.session.add(newIncome)
        db.session.commit()
        return render_template('/index.html')
    else:
        return render_template('data_form_income.html')


# 4)Data form outcome page:

@app.route('/data_form_outcome.html', methods=['GET', 'POST'])
def data_form_outcome():

    if request.method == 'POST':
        newID_user = request.form['ID_user']
        newID_vendor = request.form['ID_vendor']
        newID_category = request.form['ID_category']
        newamount_outcome = request.form['amount_outcome']
        newcurrency_outcome = request.form['currency_outcome']
        newdate_outcome = request.form['date_outcome']
        newdate_outcome1 = request.form['date_outcome1']
        newp_m_outcome = request.form['p_m_outcome']
        newcomment_outcome = request.form['comment_outcome']
        newOutcome = Outcome(newID_user, newID_vendor, newID_category, newamount_outcome,
                             newcurrency_outcome, newdate_outcome, newp_m_outcome, newcomment_outcome, newdate_outcome1)
        db.session.add(newOutcome)
        db.session.commit()
        return render_template('/index.html')
    else:
        return render_template('data_form_outcome.html')

# 5)Analysis pages:


@app.route('/analysis.html')
def analysis():
    return render_template('analysis.html')

# Analysis for jorge10:


@app.route('/jorge10.html', methods=['GET', 'POST'])
def analysisjorge10():
    db = get_db()
    cur = db.execute('SELECT(val1 - val2) \
                     FROM(SELECT ID_user, currency_income, sum(amount_income) AS val1 \
                          FROM income \
                          GROUP BY ID_user) inc \
                     JOIN(SELECT ID_user, currency_outcome, sum(amount_outcome) AS val2 \
                          FROM outcome \
                          GROUP BY ID_user) out \
                     ON(inc.ID_user=out.ID_user) \
                     WHERE out.ID_user=10 \
                        AND out.currency_outcome="pln" \
                        AND inc.currency_income="pln"')

    cur1 = db.execute('SELECT sum(outcome.amount_outcome) \
                        FROM outcome \
                        INNER JOIN user, vendor \
                            ON outcome.ID_vendor=vendor.id \
                            AND outcome.ID_user=user.id \
                        WHERE user.username="jorge10" \
                            AND vendor.vendor_name="Biedronka"')

    cur2 = db.execute('SELECT SUM(outcome.amount_outcome) \
                      FROM outcome \
                      INNER JOIN category \
                        ON outcome.ID_category=category.id \
                      WHERE outcome.ID_user=10 \
                        AND category.category_name="Parties" \
                        AND outcome.date_outcome="Dec" \
                        AND outcome.date_outcome1="2019" \
                        AND outcome.currency_outcome="pln"')

    cur3 = db.execute('SELECT ROUND(AVG(outcome.amount_outcome), 2) \
                        FROM outcome \
                        WHERE outcome.ID_category=25 \
                            AND outcome.currency_outcome="pln"')

    df3 = pd.read_sql_query('SELECT outcome.amount_outcome, outcome.currency_outcome, \
                    category.category_name, vendor.vendor_name \
                        FROM outcome \
                        INNER JOIN category, vendor, user \
                            ON outcome.ID_category=category.id \
                            AND outcome.ID_vendor=vendor.id \
                            AND outcome.ID_user=user.id \
                        WHERE user.id=10 \
                            AND outcome.date_outcome="Dec" \
                            AND outcome.date_outcome1=2019 ', connection)

    df3.rename(columns={'amount_outcome': 'Amount', 'currency_outcome': 'Currency',
                        'category_name': 'Category', 'vendor_name': 'Vendor'}, inplace=True)

    balance = cur.fetchall()
    out_cat = cur1.fetchall()
    out_cat1 = cur2.fetchall()
    avg_out = cur3.fetchall()

    return render_template('jorge10.html', balance=balance, out_cat=out_cat,
                           out_cat1=out_cat1, avg_out=avg_out, tables=[
                               df3.to_html(classes='data')],
                           titles=df3.columns.values)

# 6)Graphs page:


@app.route("/graphs.html")
def graphs():
    return render_template('graphs.html')


@app.route('/graphs1.html')
def build_plot():
    df = pd.read_sql_query('SELECT  date_outcome, SUM(outcome.amount_outcome) \
                       FROM    outcome \
                       INNER JOIN user \
                       on outcome.ID_user=user.id \
                       WHERE user.username="jorge10" \
                       AND outcome.amount_outcome \
                       AND outcome.date_outcome1=2019\
                       GROUP BY outcome.date_outcome',
                           connection)

# With the above SQL query it was created a data frame with two columns

    df.rename(columns={'date_outcome': 'Month',
                       'SUM(outcome.amount_outcome)': 'Outcome'}, inplace=True)

# The name of the columns from SQL was changed to Month and Outcome

    df.loc[df['Month'] == "Jan", 'C'] = 1
    df.loc[df['Month'] == "Feb", 'C'] = 2
    df.loc[df['Month'] == "Mar", 'C'] = 3
    df.loc[df['Month'] == "Apr", 'C'] = 4
    df.loc[df['Month'] == "May", 'C'] = 5
    df.loc[df['Month'] == "Jun", 'C'] = 6
    df.loc[df['Month'] == "Jul", 'C'] = 7
    df.loc[df['Month'] == "Aug", 'C'] = 8
    df.loc[df['Month'] == "Sep", 'C'] = 9
    df.loc[df['Month'] == "Oct", 'C'] = 10
    df.loc[df['Month'] == "Nov", 'C'] = 11
    df.loc[df['Month'] == "Dec", 'C'] = 12

# With the above code we create a new column (C), based in one condition

    dfa = df.sort_values(['C'], ascending=True)

# Finally I oredered by months, now we can delete the column, or create a new data frame with just the two first columns

    df2 = dfa[['Month', 'Outcome']].copy()

    img = io.BytesIO()

    plt.bar(df2['Month'], df2['Outcome'], color='teal')
    
    plt.title('Graph 1: Vertical bar chart of otcomes per month in 2019:')
    plt.xlabel('Month (2019)')
    plt.ylabel('Outcome (PLN)')
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == "__main__":
    # Like that we do not need to restart the server every time
    app.run(debug=True)
