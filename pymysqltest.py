import pymysql
conn = pymysql.connect(host='localhost', user='newuser', password='lab301')
conn.cursor().execute('create database newdb')
