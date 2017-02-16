from flask import Flask, request, render_template

import translate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def translate_form():
	return render_template('translate.html')

@app.route('/', methods=['POST'])
def translate_core():
	srclang = request.form['csrc']
	return render_template('translate.html', message=translate.translate(srclang), csrc=srclang)

if __name__ == '__main__':
	translate.open()
	app.run(port=8888, debug=False, host="0.0.0.0")
	translate.close()