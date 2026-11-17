
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run-python")
def run_python():

    message = "Hello! Python is now connected to HTML."

    return jsonify({
        "success": True,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
