import time

from algorithms import *
from random import randint

def main():
    variant = 11
    minimum = 10
    maximum = 1000
    count = maximum - variant * minimum
    array = [randint(minimum, maximum) for _ in range(count)]
    print("Вхідний масив", array, sep=": ")
    start_time = time.time()
    print("Масив відсортований алгоритмом вставки по спаданню", sort_insert_descending(array), sep=": ")
    end_time = time.time()
    print("Затрачено секунд на алгоритм вставки по спаданню", end_time - start_time, sep=": ")

if __name__ == '__main__':
    main()