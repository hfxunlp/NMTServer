from flask import Flask, request, render_template, send_from_directory

import translate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def translate_form():
	return render_template('translate.html')

@app.route('/', methods=['POST'])
def translate_core():
	srclang = request.form['csrc']
	return render_template('translate.html', etgt=translate.translate(srclang), csrc=srclang)

# send everything from client as static content
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	translate.poweron()
	app.run(port=8888, debug=False, host="0.0.0.0")
	translate.poweroff()
