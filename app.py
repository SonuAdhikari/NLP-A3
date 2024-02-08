from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        translator = Translator()
        translated_text = translator.translate(text, src='ne', dest='en').text
        return render_template('translated.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
