from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Show Login Page
@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():

    username = request.form['username'].strip()
    password = request.form['password'].strip()

    df = pd.read_excel("users.xlsx")

    df['Username'] = df['Username'].astype(str).str.strip()
    df['Password'] = df['Password'].astype(str).str.strip()

    print(df)
    print("Entered:", username, password)

    user = df[
        (df['Username'] == username) &
        (df['Password'] == password)
    ]

    print("Matched User:")
    print(user)

    if not user.empty:
        return redirect("/landing")

    return render_template(
        "login.html",
        error="Invalid Username or Password"
    )

# Landing Page
@app.route('/landing')
def landing():
    return render_template("index.html")


@app.route('/contact', methods=['POST'])
def contact():
    return redirect(url_for('landing') + '#contact')


if __name__ == "__main__":
    app.run(debug=True)
