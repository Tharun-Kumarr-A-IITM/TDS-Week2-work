from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

marks_data = {
    "X": 10,
    "Y": 20,
    "Z": 30
}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [marks_data.get(name, 0) for name in names]  # Default marks is 0 if name not found
    return jsonify({"marks": marks})

# Vercel requires the app to be exposed as `app`
