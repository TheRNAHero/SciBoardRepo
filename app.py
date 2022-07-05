from flask import Flask, render_template, request, url_for, flash, redirect
import secrets
app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token1

@app.route('/')
def backend():
    return render_template('index.html')
title=None
namee=None
content=None
@app.route('/processer', methods=["GET", "POST"])
def iGetItNow():
    if request.method=='POST':
        title=request.form['title']
        namee=request.form['name']
        content=request.form['body']
   
    return redirect(url_for('backend'))

if __name__ == '__main__':
    app.run()
