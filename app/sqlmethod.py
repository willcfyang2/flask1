import pymysql

mysql_conn = pymysql.Connection(user="root", passwd="123456", db="flask")
cursor = mysql_conn.cursor()


def create_database():
    cursor.execute("create database flask ")
    mysql_conn.commit()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INT UNSIGNED AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role int(1) NOT NULL default 0,
    PRIMARY KEY ( id )
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """)


create_table()


