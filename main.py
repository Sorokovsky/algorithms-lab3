from random import randint

from algorithms.base import SortingAlgorithm
from algorithms.binary_insertion_sort import BinaryInsertionSort
from algorithms.bingo_sort import BingoSort
from algorithms.buble_sort import BubleSort
from algorithms.cycle_sort import CycleSort
from algorithms.double_selection_sort import DoubleSelectionSort
from algorithms.insertion_sort import InsertionSort
from algorithms.pairwise_insertion_sort import PairwiseInsertionSort
from algorithms.pancake_sort import PancakeSort
from algorithms.selection_sort import SelectionSort
from algorithms.shaker_sort import ShakerSort
from algorithms.shell_sort import ShellSort

algorithms: list[SortingAlgorithm] = [
    InsertionSort(),
    PairwiseInsertionSort(),
    ShellSort(),
    SelectionSort(),
    BinaryInsertionSort(),
    DoubleSelectionSort(),
    BingoSort(),
    CycleSort(),
    PancakeSort(),
    BubleSort(),
    ShakerSort(),
]

def is_descending(first: int, second: int) -> bool:
    return first >= second


def generate_array() -> list[int]:
    variant = 11
    minimum = 10
    maximum = 1000
    count = maximum - variant * minimum
    return [randint(minimum, maximum) for _ in range(count)]

def main():
    array = generate_array()
    print("Вхідний масив", array)
    for algorithm in algorithms:
        result = algorithm.sort(array, is_descending)
        print(f"Відсортований масив за допомогою '{algorithm.get_name()}': {result}")
        print(f"Пройдено ітерацій: {algorithm.get_iterations_count()}")
        print(f"Виконано за {algorithm.get_processing_time()} секунд")

if __name__ == '__main__':
    main()