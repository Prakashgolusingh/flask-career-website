from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
app = Flask(__name__)

jobs = load_jobs_from_db()

@app.route('/')
def home():
  return render_template('home.html',jobs=jobs, company_name='Jovian')

@app.route('/jobs/api')
def api():
  return jsonify(jobs)

@app.route('/job/<id>')
def show_jobs(id):
  job = load_job_from_db(id)
  print(type(job))
  return render_template('jobitem.html', job=job)

if( __name__ == '__main__'):
  app.run(host ='0.0.0.0', debug=True)
