from flask import Flask, render_template, jsonify

app = Flask(__name__,
            template_folder='templatesFiles',
            static_folder='staticFiles')
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Banglaru, india',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scentiest',
    'location': 'Delhi, india',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engeener',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engeener',
    'location': 'London, USA',
    'salary': '$ 120,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovain')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
