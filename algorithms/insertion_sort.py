from typing import Callable

from algorithms.base import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування вставкою"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        for i in range(1, len(result)):
            j = i - 1
            unsorted_item = result[i]
            while j >= 0 and not is_order_correct(unsorted_item, result[j]):
                self._increment_iteration()
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = unsorted_item
        return result
