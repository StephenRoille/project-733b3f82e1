import os
import logging
import flask


app = flask.Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["GET"])
def home():
    logging.info("hello from the logger!")
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run()
