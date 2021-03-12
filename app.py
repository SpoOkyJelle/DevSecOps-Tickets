from flask import Flask, render_template, request
from flaskext.mysql import MySQL

import datetime

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_tickets'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def tickets():
  try: 
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `tickets` WHERE `solved` IS NULL")
    data = cursor.fetchall()
  except:
    print('error with database')
    data='error with database'

  return render_template('tickets.html', data=data)

@app.route("/addTicket", methods = ['POST'])
def addTicket():
  conn = mysql.connect()
  cursor = conn.cursor()

  ticketname = request.form['ticketname']
  ticketdesc = request.form['ticketdesc']

  sql = "INSERT INTO `tickets` (`ticket_name`, `ticket_description`, `created_at`) VALUES (%s, %s, %s)"
  cursor.execute(sql, (ticketname, ticketdesc, datetime.datetime.now(),))

  cursor.execute("SELECT * FROM `tickets` WHERE `solved` IS NULL")
  data = cursor.fetchall()

  return render_template('tickets.html', data=data)


@app.route("/ticket/<id>", methods=['GET'])
def removeTicket(id):
  conn = mysql.connect()
  cursor = conn.cursor()

  sql = "UPDATE `tickets` SET `solved` = '1' WHERE `id` = %s"
  cursor.execute(sql, id,)
  video = cursor.fetchall()

  cursor.execute("SELECT * FROM `tickets` WHERE `solved` IS NULL")
  data = cursor.fetchall()

  return render_template('tickets.html', data=data)
  
@app.route("/history")
def history():
  try: 
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `tickets` WHERE `solved` IS NOT NULL")
    data = cursor.fetchall()
  except:
    print('error with database')
    data='error with database'
  return render_template('history.html', data=data)

@app.route("/history/ticket/<id>", methods=['GET'])
def placeBack(id):
  conn = mysql.connect()
  cursor = conn.cursor()

  sql = "UPDATE `tickets` SET `solved` = NULL WHERE `id` = %s"
  cursor.execute(sql, id,)

  cursor.execute("SELECT * FROM `tickets` WHERE `solved` IS NOT NULL")
  data = cursor.fetchall()

  return render_template('history.html', data=data)


if __name__ == "__main__":
  app.run(debug=True)