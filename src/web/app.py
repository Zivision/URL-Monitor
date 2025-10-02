from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests


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

# 
# API endpoints
#
@app.route("/api/v1/test")
def test():
    return { 
        "status": 200,
        "time": datetime.now()
    }

@app.route("/api/v1/url/", methods=["POST"])
def get_status_code():
    data = request.json
    return jsonify(
        {
            "url": data["url"],
            "status_code": requests.get(data["url"]).status_code,
            "time": datetime.now()
        }
    )

# Wrapper function with params for development
def run_app(host="127.0.0.1", port=8080, debug=True) -> None:
    app.run(host=host, port=port, debug=debug)

