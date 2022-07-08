from flask import Flask, render_template, request, url_for, flash, redirect
import secrets
from better_profanity import profanity
import json
app=Flask(__name__)
app.config['SECRET_KEY']=secrets.token1
#This is a comment
messages=[]
#creates site
@app.route('/')
def backend():
    global messages
    #print("backend", messages)
    f=open('C:\gabrielFossner\Sciboard\posts.json')
    messages=json.load(f)
    f.close()
    #print("backend end", messages)
    return render_template('index.html', messages=messages)

#process form data

@app.route('/processer', methods=["GET", "POST"])
def iGetItNow():

    global messages
    #print("processer", messages)
    if request.method=='POST':
        title=request.form['title']
        namee=request.form['name']
        content=request.form['body']

    if title == "" or namee=="" or content=="" or profanity.contains_profanity(title) or profanity.contains_profanity(namee) or profanity.contains_profanity(content):
       pass
    else:
       messages.insert(0, {'title': title, 'name': namee, 'body':content})
       #print("processer mid", messages)
       if len(messages)>100:
         print(len(messages))
         messages.pop(len(messages)-1)
       x=json.dumps(messages)
       f=open('C:\gabrielFossner\Sciboard\posts.json', 'w')
       f.write(x)
       f.flush()
       f.close()
    #print("processer end", messages)
    return redirect(url_for('backend'))

if __name__ == '__main__':
    app.run()
