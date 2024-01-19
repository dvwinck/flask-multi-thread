import random
import time

random_numbers_list = []  # Lista global para armazenar os números


def generate_sequence():
    time.sleep(2)  # Adiciona um atraso de 5 segundos
    max_number = random.randint(1, 500)
    random_numbers_list.append([len(random_numbers_list),max_number])
    time.sleep(2)  # Adiciona um atraso de 5 segundos

    return max_number
