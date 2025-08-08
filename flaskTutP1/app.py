from flask import Flask, request, redirect, Response, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"

# login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")  # lowercase matches form input name
        password = request.form.get("password")
        
        if username == "admin" and password == "123":
            session["user"] = username  # store in session
            return redirect(url_for("welcome"))  # lowercase 'welcome' function name
        else:
            return Response("Invalid Credential, try again!", mimetype="text/plain")
    
    return """
        <h2>Login Page</h2>
        <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="text" name="password"><br>
        <input type="submit" value="Login">
        </form>
    """

# welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome! {session["user"]}!</h2>
            <a href="{url_for('logout')}">Log Out</a>
        '''
    return redirect(url_for("login"))

# logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
