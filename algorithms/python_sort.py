from typing import Callable

from algorithms.base import SortingAlgorithm


class PythonSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Вбудований метод sort"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        first = 1
        second = 2
        is_reversed = False
        if is_order_correct(second, first):
            is_reversed = True
        result = array.copy()
        result.sort(reverse=is_reversed)
        return result
