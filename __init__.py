from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)


# render main page
@app.route("/")
def showMainPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

