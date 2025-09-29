from flask import Flask, render_template
from datetime import datetime

# Setup Flask
app = Flask(__name__)

# 
# UI endpoints
#
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/info")
def info():
    return render_template("info.html")

# Test end point
@app.route("/api/test")
def test():
    return { 
        "status": 200,
        "time": datetime.now()
    }

# Wrapper function with params
def run_app(host="127.0.0.1", port=8080, debug=True) -> None:
    app.run(host=host, port=port, debug=debug)

