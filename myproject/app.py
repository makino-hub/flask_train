
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World koudai !</p>"

if __name__ == "__main__":
    app.run()
    
    
# 仮装環境に入るコマンド
# . .venv/bin/activate

# flaskを実行するコマンド
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run

