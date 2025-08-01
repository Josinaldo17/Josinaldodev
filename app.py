from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def teste():
    return redirect('https://www.josinaldodev.com')
    
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    return render_template('trabalhos.html')

@app.before_request
def force_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://'), code=301)


if __name__ == '__main__':
    app.run(debug=True)
