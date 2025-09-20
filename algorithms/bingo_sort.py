from typing import Callable

from algorithms.base import SortingAlgorithm


class BingoSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Бінго сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        right = count - 1
        while right > 0:
            current_index = 0
            for index in range(1, right + 1):
                self._increment_iteration()
                if is_order_correct(result[index], result[current_index]):
                    current_index = index
            current_item = result[current_index]
            index = 0
            while index <= right:
                self._increment_iteration()
                if result[index] == current_item:
                    result = self._swap(result, index, right)
                    right -= 1
                else:
                    index += 1
        return result
