import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Определяем переменную для записи кол-ва попыток
    count = 0
    max_number=101
    min_number=0
    # Описываем цикл в котором происходит изначальная замена начальных переменных
    while True:
      count += 1
      predict=(max_number+min_number)//2 
      if predict==number:
        break
      elif predict < number:
        min_number=predict
      else:
        max_number=predict

    return count
# RUN
game_core_v3()