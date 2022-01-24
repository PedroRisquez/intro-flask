from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba'
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'Hola mundos!'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    return 'El id del post es: ' + post_id

@app.route('/form', methods=['POST', 'GET'])
def form():
    # abort(403)
    # return redirect(url_for('post',post_id=2))
    # print(request.form['llave1'],request.form['llave2'])
    # return render_template('index.html')
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    return render_template('index.html',usuarios=usuarios)

@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')

@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "INSERT INTO Usuario (username, email) values (%s, %s)"
        values = (username, email)
        cursor.execute(sql,values)
        midb.commit()
        return redirect(url_for('form'))
    return render_template('crear.html')
