from flask import Flask, render_template

app = Flask(__name__)


jobs=[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bangluru',
    'salary':245_0000
  },
  {
    'id':2,
    'title':'SWE',
    'location':'Chennai',
    'salary':343_0000
  },
  {
    'id':3,
    'title':'Full Stack Developer',
    'location':'Noida',
    'salary':200_0000
  }
]

@app.route('/')
def home():
  return render_template('home.html',jobs=jobs, company_name='Jovian')



if( __name__ == '__main__'):
  app.run(host ='0.0.0.0', debug=True)
