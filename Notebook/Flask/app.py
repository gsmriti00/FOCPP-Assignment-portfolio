from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# --- Dummy Users (Lab 5) ---
USERS = {
    "mango": {"password": "Mango00", "role": "admin"},
    "student": {"password": "student1", "role": "user"}

}

# --- Python Functions (Lab 3) ---
def get_string_operations(name):
    return {
        "Uppercase": name.upper(),
        "Lowercase": name.lower(),
        "Reversed": name[::-1],
        "Length": len(name)
    }

def add_language(language_list, new_lang):
    if new_lang and new_lang not in language_list:
        language_list.append(new_lang.capitalize())
        return f"{new_lang.capitalize()} added successfully!"
    return "Invalid or duplicate language."

def delete_selected_languages(language_list, selected):
    if not selected:
        return "No languages selected."
    count = 0
    for lang in selected:
        if lang in language_list:
            language_list.remove(lang)
            count += 1
    return f"Deleted {count} language(s)!" if count > 0 else "No matching languages found."

def clear_languages(language_list):
    language_list.clear()
    return "All languages cleared!"

def sort_languages(language_list):
    language_list.sort()
    return "Languages sorted alphabetically!"

# --- Routes ---
@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    message, string_ops = None, None
    if request.method == 'POST':
        name = request.form.get('name')
        if name.strip():
            message = f"Hello, {name.title()}!"
            string_ops = get_string_operations(name)
        else:
            message = "Please enter a valid name."
    return render_template("greet.html", title="Greet", message=message, string_ops=string_ops)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in USERS and USERS[username]['password'] == password:
            session['username'] = username
            session['role'] = USERS[username]['role']
            return redirect(url_for('favorites'))
        else:
            message = "Invalid username or password"
    return render_template("login.html", message=message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript", "Go"]

    if 'username' not in session:
        return redirect(url_for('login'))

    is_admin = session.get('role') == 'admin'
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_lang = request.form.get('language')
            message = add_language(languages, new_lang)
        elif action == 'delete_selected' and is_admin:
            selected = request.form.getlist('selected_languages')
            message = delete_selected_languages(languages, selected)
        elif action == 'clear' and is_admin:
            message = clear_languages(languages)
        elif action == 'sort':
            message = sort_languages(languages)
        else:
            message = "Unauthorized action"

    return render_template("favorites.html", title="Favorites", languages=languages, message=message, is_admin=is_admin)

if __name__ == '__main__':
    app.run(debug=True)
