from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template("index.html")

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        return redirect(url_for('index'))
    return render_template("login.html")

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic
        return redirect(url_for('login'))
    return render_template("signup.html")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

