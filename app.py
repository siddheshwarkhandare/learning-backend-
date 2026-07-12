from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about_page():
    return "this is about page"

# This MUST be at the very bottom, without an 'if' block for now
app.run(debug=True, port=5001)