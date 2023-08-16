
from flask import Flask
from flask import render_template,g,redirect,request
import sqlite3
DATABASE = "flaskmemo.db"

app = Flask(__name__)



@app.route("/")
def top():
    memo_list = get_db().execute("select id,title,body from memo").fetchall()
    
    return render_template('index.html',memo_list = memo_list)

@app.route("/regist",methods=["GET", "POST"])
def regist():
    if request.method == 'POST':
        # 画面からのデータを取得
        title = request.form.get('title')
        body = request.form.get('body')
        db = get_db()
        db.execute("insert into memo (title,body) values(?,?)",[title,body])
        db.commit()
        return redirect('/')
    return render_template('regist.html')

@app.route('/<id>/edit',methods=["GET","POST"])
def edit(id):
    if request.method == 'POST':
        # 画面からのデータを取得
        title = request.form.get('title')
        body = request.form.get('body')
        db = get_db()
        db.execute("update memo set title=?,body=? where id=?",[title,body,id])
        db.commit()
        return redirect('/')
    post = get_db().execute(
        "select id,title,body from memo where id=?",(id,)
    ).fetchone()
    return render_template('edit.html',post=post)

@app.route('/<id>/delete',methods=["GET","POST"])
def delete(id):
    if request.method == 'POST':
        db = get_db()
        db.execute(
            "delete from memo where id=?",(id,)
        )
        db.commit()
        return redirect('/')
    post = get_db().execute(
    "select id,title,body from memo where id=?",(id,)
    ).fetchone()
    return render_template('delete.html',post=post)


if __name__ == "__main__":
    app.run()
    
# database
def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv
def get_db():
    if not hasattr(g,'sqlite_db') :
        g.sqlite_db = connect_db()
    return g.sqlite_db
    
    
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


