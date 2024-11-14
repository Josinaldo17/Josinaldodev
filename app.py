from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def teste():
    return '<h1>olaaaa</h1>'
    
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    return render_template('trabalhos.html')
