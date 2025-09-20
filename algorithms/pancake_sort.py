from typing import Callable

from algorithms.base import SortingAlgorithm


class PancakeSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Млинцеве сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        for index in range(count):
            target_index = self._find_index_by_rule(result, is_order_correct)
            self._increment_iteration()
            if target_index != index - 1:
                result[:target_index + 1] = reversed(result[:target_index + 1])
                result[:index] = reversed(result[:index])
        return result

    def _find_index_by_rule(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> int:
        target_index = 0
        for index in range(len(array)):
            self._increment_iteration()
            if array[index] > array[target_index]:
                target_index = index
        return target_index
