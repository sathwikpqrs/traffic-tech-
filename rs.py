from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for user data (you'd typically use a database in a real application)
user_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Basic validation - Check if the username is not already taken
    if any(user['username'] == username for user in user_data):
        return jsonify({'success': False, 'message': 'Username is already taken.'})

    # Store user data in-memory (you'd typically use a database)
    user_data.append({'username': username, 'password': password})

    return jsonify({'success': True, 'message': 'Registration successful.'})

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match any stored user data
    if any(user['username'] == username and user['password'] == password for user in user_data):
        return jsonify({'success': True, 'message': 'Login successful.'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials.'})

if __name__ == '__main__':
    app.run(debug=True)