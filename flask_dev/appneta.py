from flask import Flask
from urllib2 import urlopen

app = Flask(__name__)

@app.route("/")
def retrieve_page():
    f = urlopen('http://www.appneta.com')
    response_body = f.read()

    return response_body


if __name__ == "__main__":
    app.run(debug=True)
