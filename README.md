# DevSecOps-Tickets
A simple ticket system for development, operations and security.

Windows
Make sure you have pip and python installed, and a database server with the SQL file.

First download the project and extract it where you want it. Then open a terminal. To install the dependecies.

```bash
pip install -r requirements.txt 
```

```bash
python app.py
```

Then the server will be running on localhost:5000

Linux
Make sure you have pip and python installed, and a database server with the SQL file.

First clone the file from github

```bash
git clone https://github.com/SpoOkyJelle/DevSecOps-Tickets.git
cd FIND3-Monitoring
```
From here we need to activate the project.

```bash
python3 -m venv FIND3-Monitoring
source FIND3-Monitoring/bin/activate
```
Install the requirements.

```bash
pip install -r requirements.txt 
```
After that we need to install install the dependencies to run the application.

Before we can run the app we need to tell the flask app that it can allow a connection from anywhere.
```bash
sudo nano app.py
Change the following code from:
```
```python
if __name__ == "__main__":
  app.run(debug=True)
To this:
```

```python
if __name__ == "__main__":
  app.run(host='0.0.0.0')
Then we will allow the port 5000 and run the app.
```

```bash
sudo ufw allow 5000
python app.py
```
