from django.shortcuts import render
import pyodbc

em = ''
pwd = ''

def loginaction(request):
    global em, pwd
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
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        c = "SELECT * FROM users WHERE email=? AND password=?"
        cursor.execute(c, (em, pwd))
        t = cursor.fetchall()
        cursor.close()
        conn.close()
        if not t:
            return render(request, 'error.html')
        else:
            return render(request, "welcome.html")

    return render(request, 'login_page.html')
