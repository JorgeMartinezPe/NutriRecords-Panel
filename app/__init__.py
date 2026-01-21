from flask import Flask
from .extensions import db
from app.config import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # blueprints
    from app.routes.main import main_bp,logout_bp,consulta_bp
    from app.routes.home_page import home_bp
    from app.routes.errores import errores_bp
    from app.routes.register import register_bp
    from app.routes.sesion import sesion_bp
    from app.routes.agregar_paciente import agregar_paciente_bp
    from app.routes.fase2 import consulta_fase2_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(errores_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(consulta_fase2_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(sesion_bp)
    app.register_blueprint(agregar_paciente_bp)

    return app
