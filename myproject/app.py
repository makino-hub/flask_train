
from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list = [
    {'title':"test01",'body':"グラです"},
    {'title':"test02",'body':"グリです"},
    {'title':"test03",'body':"test03"}
]

@app.route("/")
def top():
    return render_template('index.html',memo_list = memo_list)



if __name__ == "__main__":
    app.run()
    
    
# 仮装環境に入るコマンド
# . .venv/bin/activate

# flaskを実行するコマンド
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run


# DB tableを繋げる時
# sqlite3 テーブル名(今回:flaskmemo.db)

# DB tableを消すとき
# drop table テーブル名;

# データを登録
# insert into memo(title,body)
# values("Second message","Hello Guri");

# データを更新
# UPDATE memo
# SET title = "update_test",
# body = "updateのテストです"
# where id = 2;

# データの削除
# DELETE from memo
# where 条件；


# DBのトラザクション管理
# BEGIN;
# SQLの処理
#rollback(処理を戻す時);or commit(処理を確定させる)


