from typing import Callable

from algorithms.base import SortingAlgorithm


class StupidSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Безглузде сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        index = 0
        while index < len(result) - 1:
            self._increment_iteration()
            if not is_order_correct(result[index], result[index + 1]):
                result = self._swap(result, index, index + 1)
                index = 0
            else:
                index += 1
        return result
