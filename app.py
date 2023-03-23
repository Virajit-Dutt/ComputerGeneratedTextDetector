from flask import Flask, request, render_template
from models import scripts

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        op = scripts.predict(text)

        op = 'Computer Generated Text' if op == 1 else 'Original Text'

        return render_template('index.html', text=text, op=op)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)