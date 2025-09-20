from typing import Callable

from algorithms.base import SortingAlgorithm


class BinaryInsertionSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування простими вставками з бінарним пошуком"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        for i in range(1, len(result)):
            key = result[i]
            position = self._binary_search(result, key, 0, i, is_order_correct)
            j = i
            while j > position:
                self._increment_iteration()
                result[j] = result[j - 1]
                j -= 1
            result[position] = key
        return result

    def _binary_search(self, array: list[int], key: int, left: int, right: int,
                       is_order_correct: Callable[[int, int], bool]) -> int:
        while left < right:
            self._increment_iteration()
            middle = (left + right) // 2
            if not is_order_correct(key, array[middle]):
                left = middle + 1
            else:
                right = middle
        return left
