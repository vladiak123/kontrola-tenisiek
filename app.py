from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("data.json", encoding="utf-8") as f:
        sneakers = json.load(f)
    return render_template("index.html", sneakers=sneakers)

if __name__ == "__main__":
    app.run(debug=True)
