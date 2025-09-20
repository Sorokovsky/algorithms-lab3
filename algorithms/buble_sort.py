from typing import Callable

from algorithms.base import SortingAlgorithm


class BubleSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування бульбашкою"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for index in range(len(result) - 1):
                self._increment_iteration()
                if not is_order_correct(result[index], result[index + 1]):
                    result = self._swap(result, index, index + 1)
                    is_sorted = False
        return result
