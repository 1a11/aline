import aruco_beta as ar
from flask import Flask,jsonify
import json
app = Flask(__name__)

@app.route("/get", methods=['GET','POST'])
def index():
    return jsonify(ar.run(), (0,0))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=666)
