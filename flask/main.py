from flask import Flask, render_template
app = Flask(__name__)


@app.route('/carousel')
def planet():
    dick = ["/static/images/mars1.jpg", "/static/images/mars2.jpg", "/static/images/mars3.jpg"]
    return render_template('base.html', items=dick)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')