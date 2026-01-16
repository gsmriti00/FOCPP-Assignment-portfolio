from flask import flask, render_template, request

app = flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template("index.html", title="Home")

# Greet route (GET & POST)
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        if not name.strip():
            message = "Please enter a valid name."
        else:
            message = f"Hello, {name}! Welcome to Flask Forms."
    return render_template("greet.html", title="Greet", message=message)

if __name__ == '__main__':
    app.run(debug=True)
