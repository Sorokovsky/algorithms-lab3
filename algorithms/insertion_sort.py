from typing import Callable

from algorithms.base import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = [item for item in array]

        return result
