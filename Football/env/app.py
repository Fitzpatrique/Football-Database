from flask import Flask, request, redirect, jsonify, render_template, url_for 
import requests

app = Flask(__name__) # set app object from flask class




@app.route('/sign-up', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        req = request.form
        print(req)

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        age = request.form['age']
        nationality = request.form['nationality']
        club = request.form['club']
        position = request.form['position']

        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/signup/form"

        payload = {"first_name" : first_name, "last_name": last_name,  "password": password,"age": age, "nationality": nationality, "club": club, "position": position}
        headers= {}
        response = requests.request("POST", url, headers = headers, data = payload)
        
        return redirect("user-profile")
    return render_template("sign-up.html")  #render_template('welcome.html')



@app.route('/update-user', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        
        req = request.form
        print(req)

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        age = request.form['age']
        nationality = request.form['nationality']
        club = request.form['club']
        position = request.form['position']

        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/profile/update/2266632219/c713c5b61d8bfa64118d998a9812ba0f"

        payload = {"update": {"first_name" : first_name, "last_name": last_name,  "password": password,"age": age, "nationality": nationality, "club": club, "position": position}}
        headers= {}
        response = requests.request("POST", url, headers = headers, data = payload)
        
        return redirect("user-profile")
    return render_template("update.html") 
    


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        req = request.form
        print(req)

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']

        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/login/user"

        payload = {"update": {"first_name" : first_name, "last_name": last_name,  "password": password}}
        headers= {}
        response = requests.request("POST", url, headers = headers, data = payload)
        
        return redirect("user-profile")
    return render_template("login.html") 
    


@app.route('/user-profile', methods=['POST','GET'])
def fetchuser():
    if request.method == "GET":
        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/profile/fetch/220043427165/17224235b53bd8c533ce4b930dee2cf2"

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        return response.text.encode('utf8')
    return render_template('user-profile.html')




@app.route('/logout', methods=['POST','GET', "PUT"])
def logout():
    if request.method == "PUT":
        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/logout/user/7e124209ba8b81fbe74cdca964d7a261"

        payload = {}
        headers= {}

        response = requests.request("PUT", url, headers=headers, data = payload)

        print(response.text.encode('utf8'))


        return redirect("login")
    return render_template('user-profile.html')




@app.route('/update-password', methods=['POST','GET', "PUT"])
def changePassword():
    if request.method == "PUT":

        req = request.form
        print(req)

        password = request.form['password']
        new_password = request.form['new_password']
        new_password = request.form['new_password']

        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/profile/changePassword/57587927138/15cc5adce658c7cd1d9f150a60ba2ca7"

        payload = {"update": {"password" : password, "new_password": new_password,  "new_password": new_password}}
        headers= {}

        response = requests.request("PUT", url, headers=headers, data = payload)

        print(response.text.encode('utf8'))


        return redirect("user-profile")
    return render_template('update-password.html')




@app.route('/delete-user', methods=['POST','GET', "PUT"])
def deleteuser():
    if request.method == "GET":

        url = "http://ec2-3-95-53-126.compute-1.amazonaws.com:3700/profile/delete/5374186468/0181ead79a4ddd41f806aab00d7b2826"

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        
        return redirect("login")
    return render_template('user-profile.html')

if __name__ == "__main__":
    app.run(debug=True)