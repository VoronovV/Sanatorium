import sqlite3

from sqlite3 import *


def db_connection():
    try:
        con = sqlite3.connect('database.db')
        print("has created")
        return con
    except Error:
        print(Error)


def create_db(con):
    obj = con.cursor()
    obj.execute("create table if NOT EXISTS users(id integer PRIMARY KEY, login text, password text)")
    con.commit()

def add_in_users_table(con, login, password):
    obj = con.cursor()
    obj.execute("INSERT INTO users (login, password) values(?, ?)", (login, password))
    con.commit()

def login_in_users_table(con, login, password):
    obj = con.cursor()

    if len(obj.execute("select login, password from users where login = ? and password = ?", (login, password)).fetchall()) > 0:
        return True
    else:
        print("not found")