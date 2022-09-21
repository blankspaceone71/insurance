from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('indexx.html')


@app.route('/math', methods=['POST'])
def predict():
    if request.method == "POST":
        age = int(request.form['a'])
        sex = int(request.form['se'])
        bmi = int(request.form['b'])
        child = int(request.form['c'])
        smoker = int(request.form['s'])
        region = int(request.form['r'])

        try:
            r = [age, sex, bmi, child, smoker, region]

            result = util.insurance_prediction(r)
            result1 = 'The insurance cost is USD={}'.format(result)
            return render_template('indexx.html', prediction=result1)

        except :
            return "Something is wrong"


if __name__ == "__main__":
    app.run(debug=True)
