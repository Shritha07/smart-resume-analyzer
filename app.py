from flask import Flask, render_template, request
from analyzer import analyze_resume

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyzer")
def analyzer():
    return render_template("analyzer.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form["resume"]
    job_desc = request.form["job"]

    result = analyze_resume(resume, job_desc)
    return render_template("result.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
