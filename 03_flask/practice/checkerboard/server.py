from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",row = 8, col=8)

@app.route('/4')
def index_4():
    return render_template("index.html",row = 8, col=4)

@app.route('/<int:row>/<int:col>')
def index_row_col(row,col):
    return render_template("index.html",row = row, col=col)
@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def index_row_col_color(row,col,color1,color2):
    return render_template("index.html",row = row, col=col ,color1=color1,color2=color2)



if __name__ == "__main__" :
    app.run(debug = True,host = "localhost")