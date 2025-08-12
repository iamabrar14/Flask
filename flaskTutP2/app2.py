from flask import Flask,render_template,request

app= Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit", methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
   
    valid_users={
           'admin':'123',
           'abrar':'rahman',
           'anik':'mahmud',
           'akib':'hasan'
           }
    if username in valid_users and password==valid_users[username]:
           return render_template("welcome.html",name=username)
    else:
           return "Invalid Credentials!"
    
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)