from typing import Callable

from algorithms.base import SortingAlgorithm


class GnomeSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування Гнома"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        index = 0
        while index < len(result):
            self._increment_iteration()
            if index == 0 or is_order_correct(result[index - 1], result[index]):
                index += 1
            else:
                result = self._swap(result, index - 1, index)
                index -= 1
        return result
