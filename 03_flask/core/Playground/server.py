from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return "Playground Core Assignement"
@app.route("/play")
def play():
    return render_template("index.html",boxe=3)

@app.route("/play/<int:boxe>")
def play_boxes(boxe):
    return render_template("index.html",boxe=boxe)

@app.route("/play/<int:boxe>/<color>")
def play_boxes_color(boxe,color):
    return render_template("index.html",boxe=boxe , color = color )


if __name__ == "__main__" :
    app.run(debug = True)