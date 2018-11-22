from flask import Flask,render_template
import mysql.connector

app = Flask(__name__, template_folder='Templates')

emps = [
    {'id': '101','name':'Aravind'},
    {'id':'102','name':'Ravi'},
    {'id':'103','name':'Raju'},
    {'id':'104','name':'Ramesh'},
    {'id':'105','name':'Shiva'},
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',title='Home Page',emps=emps)

@app.route('/emps')
def employees():
    conn = mysql.connector.connect(user='root', password='2856',
                                   host='127.0.0.1',
                                   database='aravind')

    cursor = conn.cursor()
    cursor.execute("select * from emps")
    result = cursor.fetchall()
    return render_template('emps.html',title='Employees',result=result)

@app.route('/about')
def about():
    return render_template('about.html',title="About Page")


if __name__ == '__main__':
    app.run(debug=True)