from typing import Callable

from algorithms.base import SortingAlgorithm


class AnalyzerNode:
    def __init__(self, algorithm: SortingAlgorithm, comparer: Callable[[int, int], bool]):
        self.algorithm = algorithm
        self.comparer = comparer
