from flask import Flask, render_template, jsonify
from database import load_data_from_db
app = Flask(__name__)




jobs = load_data_from_db()


@app.route('/')
def home():
  return render_template('home.html',jobs=jobs, company_name='Jovian')

@app.route('/api/jobs')
def api():
  return jsonify(jobs)

if( __name__ == '__main__'):
  app.run(host ='0.0.0.0', debug=True)
