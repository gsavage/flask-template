"""Flask application factory."""

from flask import Flask


def create_app(config: dict | None = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Load configuration
    if config:
        app.config.update(config)

    # Register blueprints and routes
    from app.routes import register_routes

    register_routes(app)

    return app
