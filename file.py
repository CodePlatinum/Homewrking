from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'Привіт, {name}!'

if __name__ == '__main__':
    app.run(debug=True)

#<form> — тег, який створює форму.                                           ALL THIS IN HMTL FILE

#method="POST" — означає, що дані відправляються методом POST.

#action="/submit" — URL, на який будуть відправлені дані.

#<input> — поле для введення тексту.

#<button> — кнопка для відправки форми.
