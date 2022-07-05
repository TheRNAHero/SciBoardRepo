from flask import Flask, render_template, request, url_for, flash, redirect
import secrets
app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token1
messages=[]
@app.route('/')
def backend():
    return render_template('index.html', messages=messages)

@app.route('/criminal')
def criminal():
    return render_template('criminal.html')

@app.route('/processer', methods=["GET", "POST"])
def iGetItNow():
    if request.method=='POST':
        title=request.form['title']
        namee=request.form['name']
        content=request.form['body']

    if title == "" or namee=="" or content=="":
       pass
    else:
       messages.insert(0, {'title': title, 'name': namee, 'body':content})
    return redirect(url_for('backend'))

if __name__ == '__main__':
    app.run()
