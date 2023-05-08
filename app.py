from flask import Flask, render_template, request, session
import mysql.connector
from flask_mysqldb import MySQL 



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')    

@app.route('/register')
def register():
    return render_template('register_page.html')

@app.route('/hregi')
def hregi():
    return render_template('hospital_admin.html')



# import pymysql

# # database connection
# connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="test")
# cursor = connection.cursor()
# # some other statements  with the help of cursor
# print(connection)



# @app.route('/login_validation', methods=['POST'])
# def login_validation():
#     if request.method=="POST":
#         hospitalname=request.form.get('name')
#         password=request.form.get('psw')
#         session['email']= email 
        

#         cursor.execute("""SELECT * FROM `login` WHERE `hospitalname` LIKE {} AND `password` LIKE {}""".format(hospitalname, password))

#         user=cursor.fetchall()
#         print(user)

#         return render_template('/hregi')


# @app.route('/add_user', methods=['post'])
# def add_user():
#     hospitalname=request.form.get('hname')
#     email=request.form.get('hemail')
#     password=request.form.get('hpassword')
#     address=request.form.get('haddress')
#     city=request.form.get('hcity')

#     cursor.execute("""INSERT INTO `login` (`hospitalname`, `email`, `password`, `address`, `city`) VALUES (NULL, '{}', '{}', '{}')""".format(hospitalname,email,password,address,city))
#     connection.commit()
#     return render_template('login_page.html')
# connection.close()












@app.route('/logout')
def logout():
    
    return render_template('login_page.html') 
   


if __name__=="__main__":
    app.run(debug=True)    