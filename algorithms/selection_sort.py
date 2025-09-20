from typing import Callable

from algorithms.base import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування вибіркою"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        for i in range(count):
            extreme_index = i
            for j in range(i + 1, count):
                self._increment_iteration()
                if not is_order_correct(result[extreme_index], result[j]):
                    extreme_index = j
            if extreme_index != i:
                result = self._swap(result, extreme_index, i)
        return result
