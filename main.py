from random import randint

from algorithms.base import SortingAlgorithm
from algorithms.insertion_sort import InsertionSort


def is_descending(first: int, second: int) -> bool:
    return first < second


algorithms: list[SortingAlgorithm] = [InsertionSort()]

def main():
    variant = 11
    minimum = 10
    maximum = 1000
    count = maximum - variant * minimum
    array = [randint(minimum, maximum) for _ in range(count)]
    print("Вхідний масив", array)
    for algorithm in algorithms:
        result = algorithm.sort(array, is_descending)
        print(f"Відсортований масив за допомогою '{algorithm.get_name()}': {result}")
        print(f"Пройдено ітерацій: {algorithm.get_iterations_count()}")
        print(f"Виконано за {algorithm.get_processing_time()} секунд")

if __name__ == '__main__':
    main()