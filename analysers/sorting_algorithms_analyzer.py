from typing import Callable

from algorithms.base import SortingAlgorithm
from analysers.analyzer_node import AnalyzerNode


class SortingAlgorithmsAnalyzer:
    _nodes: list[AnalyzerNode] = []

    def add_algorithm(self, algorithm: SortingAlgorithm, comparer: Callable[[int, int], bool]) -> None:
        self._nodes.append(AnalyzerNode(algorithm, comparer))

    def run(self, array: list[int] = None):
        if array is None:
            array = [3, 2, 1, 5, 4]
        print("Вхідний масив: ", array)
        for node in self._nodes:
            result = node.algorithm.sort(array, node.comparer)
            print(f"Масив відсортовано алгоритмом '{node.algorithm.get_name()}': {result}")

    def print_statistics(self):
        print("Статистика алгоритмів сортування")
        for node in self._nodes:
            print(f"{node.algorithm.get_name()}: ")
            print(f"Кількість ітерацій: {node.algorithm.get_iterations_count()}")
            print(f"Виконано за {round(node.algorithm.get_processing_time(), 3)} секунд")

    @staticmethod
    def _default_comparator(first: int, second: int) -> bool:
        return first <= second
