# DevSecOps-Tickets
A simple ticket system for development, operations and security.

Windows
Make sure you have pip and python installed, and a database server with the SQL file.

First download the project and extract it where you want it. Then open a terminal. To install the dependecies.

pip install -r requirements.txt 
python app.py
Then the server will be running on localhost:5000

Linux
Make sure you have pip and python installed, and a database server with the SQL file.

First clone the file from github

git clone https://github.com/SpoOkyJelle/DevSecOps-Tickets.git
cd FIND3-Monitoring
From here we need to activate the project.

python3 -m venv FIND3-Monitoring
source FIND3-Monitoring/bin/activate
Install the requirements.

pip install -r requirements.txt 
After that we need to install install the dependencies to run the application.

pip install wheel
pip install gunicorn flask
Before we can run the app we need to tell the flask app that it can allow a connection from anywhere.

sudo nano app.py
Change the following code from:

if __name__ == "__main__":
  app.run(debug=True)
To this:

if __name__ == "__main__":
  app.run(host='0.0.0.0')
Then we will allow the port 5000 and run the app.

sudo ufw allow 5000
python app.py