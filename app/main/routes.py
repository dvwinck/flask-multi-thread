from flask import jsonify, current_app
from . import main
import random
import time
from ..utils import generate_sequence, random_numbers_list


@main.route('/random_number', methods=['GET'])
def random_numbers():
    current_app.logger.info(f' Inciando')
    numbers = generate_sequence()
    current_app.logger.info(f' Finalizando')
    time.sleep(1)
    return jsonify(numbers)


@main.route('/numbers_list', methods=['GET'])
def get_numbers_list():
    return jsonify(random_numbers_list)
