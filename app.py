from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def teste():
    return redirect('/home')
    
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    return render_template('trabalhos.html')

