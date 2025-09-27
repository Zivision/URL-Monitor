from flask import Flask

# Setup Flask
app = Flask(__name__)

# Home Route
@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"

# Wrapper function with params
def run_app(host="127.0.0.1", port=8080, debug=True) -> None:
    app.run(host=host, port=port, debug=debug)

