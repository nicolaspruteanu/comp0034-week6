from flask import Flask


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)
    with app.app_context():
        from . import hello
    app.config["SECRET_KEY"] = "XbBAdmhDPz3BH1-rwPkzNg"

    return app