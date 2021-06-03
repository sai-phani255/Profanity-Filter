from flask import Flask, render_template, request
import pickle
from profanityfilter import ProfanityFilter
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
  pf=ProfanityFilter()
  if request.method == 'POST':
    message = request.form['message']
    a=pf.censor(message)
    return render_template('result.html',a = a,message = message)

if __name__ == '__main__':
	app.run()
