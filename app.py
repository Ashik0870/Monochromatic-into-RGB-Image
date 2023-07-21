from distutils.log import debug
from fileinput import filename
from flask import *
app = Flask(__name__)
import os


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response
    
@app.route('/')
def main():
	return render_template("index.html")

@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save('original.jpeg')
		os.system('python ./demo_release.py')
		return render_template("converted.html", name = f.filename)

if __name__ == '__main__':
	app.run(debug=True)
