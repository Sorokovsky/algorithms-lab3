from typing import Callable

from algorithms.base import SortingAlgorithm


class PancakeSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Млинцеве сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        if count <= 1:
            return result
        for i in range(count - 1, -1, -1):
            target_index = self._find_index_by_rule(result, is_order_correct, i + 1)
            self._increment_iteration()
            if target_index != i:
                if target_index != 0:
                    result[:target_index + 1] = reversed(result[:target_index + 1])
                    self._increment_iteration()
                if i > 0:
                    result[:i + 1] = reversed(result[:i + 1])
                    self._increment_iteration()
        return result

    def _find_index_by_rule(self, array: list[int], is_order_correct: Callable[[int, int], bool], size: int) -> int:
        target_index = 0
        for index in range(size):
            self._increment_iteration()
            if not is_order_correct(array[index], array[target_index]):
                target_index = index
        return target_index
