from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET"])
def root():
   return "Welcome to Version1"
app.run(host="0.0.0.0",port=4010, debug=True)
