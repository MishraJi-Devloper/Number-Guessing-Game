# Number Guessing Game (Flask)

A simple web-based number guessing game built with Flask and modern HTML/CSS/JS.

## Features

- Unlimited attempts to guess a random number between 1 and 100
- Modern UI with animated "Hurrah!" popup on correct guess
- Responsive and mobile-friendly

## Running Locally

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/number_guessing_game.git
   cd number_guessing_game
   ```

2. **Create a virtual environment and install dependencies:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app:**
   ```
   python number_guessing_game/number_guessing_game.py
   ```

4. **Open your browser and go to:**  
   `http://127.0.0.1:5000/`

## Deployment

- For public hosting, use [Render](https://render.com/), [PythonAnywhere](https://www.pythonanywhere.com/), or [Heroku](https://heroku.com/).
- GitHub Pages does **not** support Python/Flask backend.  
  For static hosting only, copy the contents of `templates/index.html` and `static/` to a `docs/` folder and remove backend logic.

---
