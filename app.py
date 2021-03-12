from flask import Flask, render_template
from flaskext.mysql import MySQL

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

if __name__ == "__main__":
  app.run(debug=True)