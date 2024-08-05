from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import pyodbc

fn = ''
ln = ''
s = ''
em = ''
pwd = ''

def signaction(request):
    global fn, ln, s, em, pwd
    if request.method == "POST":
        conn = pyodbc.connect(
            #'driver={ODBC Driver 17 for SQL Server};'
            'HOST=localhost;'
            'DATABASE=sa;'
            'USER=sa;'
            'PASSWORD=--JaiShreeGanesh#1'
        )
        cursor = conn.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        c = "INSERT INTO users (first_name, last_name, sex, email, password) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(c, (fn, ln, s, em, pwd))
        conn.commit()
        cursor.close()
        conn.close()

    return render(request, 'signup_page.html')
