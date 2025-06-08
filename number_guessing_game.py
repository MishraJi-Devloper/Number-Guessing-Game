from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure random key

@app.route('/')
def index():
    # Initialize target number in session if not present
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    try:
        guess = int(data.get('guess'))
    except (ValueError, TypeError):
        return jsonify({'message': 'Invalid input! Please enter a number.'}), 400

    # Get target number from session, set if missing
    target_number = session.get('target_number')
    if target_number is None:
        target_number = random.randint(1, 100)
        session['target_number'] = target_number

    if guess < target_number:
        message = 'Too low!'
    elif guess > target_number:
        message = 'Too high!'
    else:
        message = 'Correct! You guessed it!'
        session['target_number'] = random.randint(1, 100)  # reset the number

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
