import os
import logging
import flask


app = flask.Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["GET"])
def home():
    logging.info("hello from the logger!")
    name = os.environ.get("NAME", "No Name provided")
    return flask.render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()
