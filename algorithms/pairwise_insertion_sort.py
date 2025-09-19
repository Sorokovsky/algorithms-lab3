from typing import Callable

from algorithms.base import SortingAlgorithm


class PairwiseInsertionSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування парними вставками"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)

        for i in range(0, count, 2):
            if i + 1 < count:
                self._increment_iteration()
                if not is_order_correct(result[i + 1], result[i]):
                    result[i], result[i + 1] = result[i + 1], result[i]
            self._insert_pair(result, i, is_order_correct)

        return result

    def _insert_pair(self, array: list[int], start_index: int, is_order_correct: Callable[[int, int], bool]) -> None:
        if start_index == 0:
            return
        if start_index + 1 < len(array):
            temp_first = array[start_index]
            temp_second = array[start_index + 1]
        else:
            temp_first = array[start_index]
            temp_second = None
        j = start_index - 1
        if temp_second is not None:
            while j >= 0 and not is_order_correct(temp_second, array[j]):
                self._increment_iteration()
                array[j + 2] = array[j]
                j -= 1
            array[j + 2] = temp_second
        current_j = j if temp_second is not None else start_index - 1
        while current_j >= 0 and not is_order_correct(temp_first, array[current_j]):
            self._increment_iteration()
            array[current_j + 1] = array[current_j]
            current_j -= 1
        array[current_j + 1] = temp_first