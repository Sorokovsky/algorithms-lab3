from typing import Callable

from algorithms.base import SortingAlgorithm


class ShakerSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Шейкер-сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        start = 0
        end = len(array) - 1
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for index in range(start, end):
                self._increment_iteration()
                if not is_order_correct(result[index], result[index + 1]):
                    result = self._swap(result, index, index + 1)
                    is_sorted = False
            end -= 1
            if is_sorted:
                break
            for index in range(end, start, -1):
                self._increment_iteration()
                if not is_order_correct(result[index - 1], result[index]):
                    result = self._swap(result, index - 1, index)
                    is_sorted = False
            start += 1
        return result
