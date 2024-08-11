from flask import Flask, render_template, request, jsonify

#import other file dependencies


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/queries/llm')
def queries_llm():
    return render_template('queries/llm_queries.html')


if __name__ == '__main__':
    app.run(debug=True)
