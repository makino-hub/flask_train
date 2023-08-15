
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_guri():
    return render_template('index.html')

# @app.route("/<name>")
# def hello(name):
#     return f"<p>Hello, {name} !</p>"





if __name__ == "__main__":
    app.run()
    
    
# 仮装環境に入るコマンド
# . .venv/bin/activate

# flaskを実行するコマンド
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run

