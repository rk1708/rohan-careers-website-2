from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Munich, Germany',
    'salary': '70,000 Euros'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '80,000 Euros'
}, {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company='Rohan')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
