from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>Hello Bitches!</h1>"

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
