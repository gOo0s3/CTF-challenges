from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    expression_to_calculate = request.form.get("expression_to_calculate", type=str)

    try:
        return str(eval(expression_to_calculate))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337, debug=True)
