from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("BD1.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from clientes")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/agregar_cliente",methods=['POST','GET'])
def agregar_cliente():
    if request.method=='POST':
        uid=request.form['uid']
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("BD1.db")
        cur=con.cursor()
        cur.execute("insert into clientes(UID,UNAME,CONTACT) values (?,?,?)",(uid,uname,contact))
        con.commit()
        flash('Usuario Agregado','success')
        return redirect(url_for("index"))
    return render_template("agregar_cliente.html")

@app.route("/editar_cliente/<string:uid>",methods=['POST','GET'])
def editar_cliente(uid):
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("BD1.db")
        cur=con.cursor()
        cur.execute("update clientes set UNAME=?,CONTACT=? where UID=?",(uname,contact,uid))
        con.commit()
        flash('Usuario Actualizado','success')
        return redirect(url_for("index"))
    con=sql.connect("BD1.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from clientes where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("editar_cliente.html",datas=data)
    
@app.route("/eliminar_cliente/<string:uid>",methods=['GET'])
def eliminar_cliente(uid):
    con=sql.connect("BD1.db")
    cur=con.cursor()
    cur.execute("delete from clientes where UID=?",(uid,))
    con.commit()
    flash('Usuario Eliminado','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)