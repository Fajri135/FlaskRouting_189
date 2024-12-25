from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page (login form)
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')  # Ambil data dari form input
    return render_template('submit.html', user_input=user_input)  # Render halaman hasil

if __name__ == '__main__':
    app.run(debug=True)