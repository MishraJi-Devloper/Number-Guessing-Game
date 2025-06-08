from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__)

# Set a secure secret key (in production, store this in an environment variable)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'replace_this_with_a_strong_secret_key')

@app.route('/')
def index():
    # Set a random target number in the session if it's not already set
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()

    if not data or 'guess' not in data:
        return jsonify({'message': 'No guess provided!'}), 400

    try:
        guess = int(data['guess'])
    except (ValueError, TypeError):
        return jsonify({'message': 'Invalid input! Please enter a valid number.'}), 400

    target_number = session.get('target_number', random.randint(1, 100))
    session['target_number'] = target_number  # Ensure it's set

    if guess < target_number:
        message = 'Too low!'
    elif guess > target_number:
        message = 'Too high!'
    else:
        message = 'Correct! You guessed it!'
        session['target_number'] = random.randint(1, 100)  # Reset for next game

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
