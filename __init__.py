from flask import Flask, render_template, request, redirect
# import main.py


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    from . import db
    db.init_app(app)

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/failed_email')
def failed_email():
    return render_template('failed_email.html')


@app.route('/test.py', methods=['POST'])
def run_spammer():
    if request.method == 'POST':
        _email = (request.form.get('email'))
    if '@' in _email and '.' in _email:
        return redirect('/generating_spam')
    else:
        return redirect('/failed_email')


@app.route('/generating_spam')
def acquiring_spam():
    return render_template('processing.html')


if __name__ == '__main__':
    app.run(debug=True)
