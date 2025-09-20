from typing import Callable

import matplotlib.pyplot as pyplot

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

    def show_statistics_in_histograms(self):
        pyplot.figure(figsize=(12, 5))
        colors = ["skyblue", "lightgreen", "lightpink"]
        pyplot.subplot(1, 2, 1)
        for index, node in enumerate(self._nodes):
            algorithm = node.algorithm
            pyplot.hist(algorithm.get_processing_time(), bins=10, alpha=0.5, color=colors[index],
                        label=algorithm.get_name(), edgecolor="black")
        pyplot.title("Гістограма за часом")
        pyplot.xlabel("Назва алгоритму")
        pyplot.ylabel("Час (с)")
        pyplot.legend()
        pyplot.subplot(1, 2, 2)
        for index, node in enumerate(self._nodes):
            algorithm = node.algorithm
            pyplot.hist(algorithm.get_iterations_count(), bins=10, alpha=0.5, color=colors[index],
                        label=algorithm.get_name(), edgecolor='black')
        pyplot.title('Гістограма кількості ітерацій')
        pyplot.xlabel('Назва алгоритму')
        pyplot.ylabel('Кількість ітерацій')
        pyplot.legend()
        pyplot.tight_layout()
        pyplot.show()
    @staticmethod
    def _default_comparator(first: int, second: int) -> bool:
        return first <= second
