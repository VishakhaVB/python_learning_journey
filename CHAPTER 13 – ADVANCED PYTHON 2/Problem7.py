# 7. Explore the 'Flask' module and create a web server using Flask & Python.

# Simple Flask app demo (requires Flask installed):
try:
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello from Flask'

    if __name__ == '__main__':
        app.run(port=5000)
except Exception:
    print('Flask not installed — install with pip install Flask to run the demo')
