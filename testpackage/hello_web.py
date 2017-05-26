#! /usr/local/bin/python3

# -*- coding:utf-8 -*-

# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return [b'<h1>hello web!</h1>']


from flask import Flask
from flask import request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    # return '<h1>home</h1>'
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    # return '''<form action='signin' method='post'>
    #         <p><input name='username'></p>
    #         <p><input name='password'></p>
    #         <p><button type='submit'>signin</button></p>
    #         </form> '''
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username =='admin' and password =='password':
        # return '<h2>hello admin<h2>'
        return render_template('signin-ok.html',username=username)
    # return '<h3>fuck u</h3>'
    return render_template('form.html',message='bad username',username=username)

if __name__ == '__main__':
    app.run()
