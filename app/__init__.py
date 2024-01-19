from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import os


def create_app():
    app = Flask(__name__)
    app.logger.handlers = []

    # Configuração de Logging
    if not os.path.exists('logs'):
        os.mkdir('logs')

    logging_format = '%(asctime)s %(levelname)s: [%(threadName)s] %(message)s [in %(pathname)s:%(lineno)d]'

    # # Configuração do log para arquivo
    file_handler = RotatingFileHandler('logs/meuapp.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(logging_format))
    file_handler.setLevel(logging.INFO)

    # Configuração do log para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(logging_format))
    console_handler.setLevel(logging.INFO)

    # Adicionando ambos os handlers ao logger do Flask
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Iniciando aplicativo')

    from app.main import routes
    app.register_blueprint(routes.main)

    return app
