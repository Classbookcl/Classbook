from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/como_funciona')
def como_funciona():
    return render_template('como_funciona.html')

if __name__ == '__main__':
    app.run(debug=True)
