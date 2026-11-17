from flask import Flask, jsonify
import python

app = Flask(__name__)

@app.route("/")
def home():
    return "Website is running!"

@app.route("/run-python")
def run_python():

    result = python.my_function()

    return jsonify({
        "result": result
    })

if __name__ == "__main__":
    app.run()
