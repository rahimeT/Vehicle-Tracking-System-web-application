from concurrent.futures import thread
from msilib.schema import Icon
from sqlite3 import connect
from django.shortcuts import render
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from wtforms import Form, StringField,PasswordField
from flask_mysqldb import MySQL
from functools import wraps
import datetime ,folium, pandas as pd
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://rahime:1234@cluster0.zgvso.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect = False)

db = cluster["vehicle"]
collection  = db["R"]
collectionB = db["B"]


#Kullanıcı giriş decaroter
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için giriş yapınız.","danger")
            return redirect(url_for("login"))    
    return decorated_function


class LoginForm(Form):
    username = StringField("Username: ")
    password = PasswordField("Password: ")


app = Flask(__name__)
app.secret_key = "webApp"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "vehicletrackingsystem"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


#Url'ler
@app.route("/")
def index():
    return render_template("index.html",)

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/login",methods= ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = request.form['username']
        password_entered = request.form["password"]
        logintime = datetime.datetime.now()
        cursor = mysql.connection.cursor()
        sorgu= "Select * From users where userName = %s" 
        result = cursor.execute(sorgu, (username,)) #kullanıcı var mı kontrolü..


        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if password_entered == real_password:
                flash("Başarıyla giriş yaptınız...","success")
                
                sorgu2 = "UPDATE users SET logintime = %s WHERE userName= %s "
                cursor.execute(sorgu2,(logintime,username))
                mysql.connection.commit()

                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash("Parolanızı Yanlış girdiniz...","danger")
                return redirect(url_for("login"))    
        else:
            flash("Hatali Giriş","danger")
            return redirect(url_for("login"))  
        
    return render_template("login.html",form = form)


@login_required
@app.route("/myVehicle")
def vehicleDetail():
    cursor = mysql.connection.cursor()
    sorgu = "Select vehicleId,vehicleId2 From users where userName = %s "
    result = cursor.execute(sorgu, (session["username"],))
    if result > 0:
        data = cursor.fetchone()
    return render_template("myVehicle.html",data = data)


n = folium.Map(location=[59.334591,18.063240], tiles="OpenStreetMap", zoom_start=10)
@app.route("/map/<string:id>")
@login_required
def map(id):
  loc = []
  if session["username"] == "rahime":
      for i in collection.find():
         if i["vehicleId"] == int(id):
          lat = i["Latitude"]
          lon = i["Longtitude"]
          tooltip = i["Time"]
          loc.append([lat,lon])
          marker = folium.Marker(
          location=[lat, lon],
          popup=("Latitude:{}".format(lat),"Latitude:{}".format(lon),"time:{}".format(tooltip)),
          icon = folium.Icon(color='darkpurple'),
          tooltip=tooltip)
          marker.add_to(n)
          plot = folium.PolyLine(loc,
                color='red',
                weight=2.5, 
                opacity=0.6)
          plot.add_to(n)
         
  else:
      locB = []
      for i in collectionB.find():
         if i["vehicleId"] == int(id):
          lat = i["Latitude"]
          lon = i["Longtitude"]
          tooltip = i["Time"]
          locB.append([lat,lon]) #latitude longtitude listesi
          marker = folium.Marker(
          location=[lat, lon],
          icon = folium.Icon(color='rea'),
          popup=("Latitude:{}".format(lat),"Longtitude:{}".format(lon),"time:{}".format(tooltip)),
          tooltip=tooltip)
          marker.add_to(n)
          plot = folium.PolyLine(locB,
                color='blue',
                weight=2.5, 
                opacity=0.6)
          plot.add_to(n)
          
  return n._repr_html_()

@app.route("/map")
def MAP():
  map = folium.Map(location=[59.334591,18.063240], tiles="OpenStreetMap", zoom_start=10)
  for i in collection.find():
          lat = i["Latitude"]
          lon = i["Longtitude"]
          tooltip = i["Time"]
          marker = folium.Marker(
          location=[lat, lon],
          popup=("Latitude:{}".format(lat),"Latitude:{}".format(lon),"time:{}".format(tooltip)),
          icon = folium.Icon(color='orange'),
          tooltip=tooltip)
          marker.add_to(map)
  for i in collectionB.find():
          lat = i["Latitude"]
          lon = i["Longtitude"]
          tooltip = i["Time"]
          marker = folium.Marker(
          location=[lat, lon],
          popup=("Latitude:{}".format(lat),"Latitude:{}".format(lon),"time:{}".format(tooltip)),
          icon = folium.Icon(color='darkblue'),
          tooltip=tooltip)
          marker.add_to(map)

  return map._repr_html_()      

@app.route("/logout")
def logout():
    cursor = mysql.connection.cursor()
    logoutTime = datetime.datetime.now()
    sorgu2 = "UPDATE users SET logoutTime = %s WHERE userName= %s "
    cursor.execute(sorgu2,(logoutTime,session["username"]))
    mysql.connection.commit()
    session.clear()
    flash("Başarıyla Çıkış Yaptınız", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)