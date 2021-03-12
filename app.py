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
    cursor.execute("SELECT * FROM `tickets`")
    data = cursor.fetchall()
  except:
    print('error with database')
    data='error with database'

  return render_template('tickets.html', data=data)

@app.route("/addTicket", methods = ['POST'])
def addTicket():
  conn = mysql.connect()
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM `tickets`")
  data = cursor.fetchall()

  ticketname = request.form['ticketname']
  ticketdesc = request.form['ticketdesc']

  sql = "INSERT INTO `tickets` (`ticket_name`, `ticket_description`, `created_at`) VALUES (%s, %s, %s)"
  cursor.execute(sql, (ticketname, ticketdesc, datetime.datetime.now(),))

  return render_template('tickets.html', data=data)
  

if __name__ == "__main__":
  app.run(debug=True)