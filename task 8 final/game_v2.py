"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Задаем счетчик количества попыток
    count = 0
    # Зададим начальные минимальное и максимальное значения 
    max_num = 101
    min_num = 1
    predict_num = max_num // 2
    
    while True:
        count +=1
        
        # Проверяем меньше ли загаданное число, чем предполагаемое   
        if predict_num > number:
            max_num = predict_num
            predict_num = (min_num + max_num)//2
        
        # # Проверяем больше ли загаданное число, чем предполагаемое   
        elif predict_num < number:
            min_num = predict_num
            predict_num = (min_num + max_num)//2
        
        else:
            break
        
    #print(f"Число отгаданно за {count} попыток")        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)