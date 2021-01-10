from flask import Flask, Response, render_template, request
import json
import markdown

app = Flask(__name__)
lastval = ''

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/mk', methods=[ 'POST' ])
def gen():
    global lastval

    print (request.form)

    mk_text = (request.form['text'])
    print (mk_text)
    html = markdown.markdown(mk_text, extensions=['tables'])

    print (F" html = {html} and lastval = {lastval}")
    if html != lastval:
        lastval = html
    else:
        html = ''
    return Response( html )

app.run(threaded=True)
