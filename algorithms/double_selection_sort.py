from typing import Callable

from algorithms.base import SortingAlgorithm


class DoubleSelectionSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Двохстороння перестановка вибором"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        left = 0
        right = count - 1
        while left < right:
            minimum_index = left
            maximum_index = left
            for i in range(left + 1, right + 1):
                self._increment_iteration()
                if not is_order_correct(result[i], result[minimum_index]):
                    minimum_index = i
                if is_order_correct(result[i], result[maximum_index]):
                    maximum_index = i
            result[left], result[minimum_index] = result[minimum_index], result[left]
            if maximum_index == left:
                maximum_index = minimum_index
            result[right], result[maximum_index] = result[maximum_index], result[right]
            left += 1
            right -= 1
        return result
