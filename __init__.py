from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configurações
    app.config.from_object('config.Config')

    # Registro de rotas
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
