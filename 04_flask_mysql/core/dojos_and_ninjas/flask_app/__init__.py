from flask import Flask

app = Flask(__name__)

app.secret_key ='khrat-demo'
DATABASE = 'dojos_and_ninja_db'