from typing import Callable

from algorithms.base import SortingAlgorithm


class ShellSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування Шелла"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)

        gap = 1
        while gap < count // 3:
            gap = 3 * gap + 1

        while gap >= 1:
            for i in range(gap, count):
                temp = result[i]
                j = i
                while j >= gap and not is_order_correct(result[j - gap], temp):
                    self._increment_iteration()
                    result[j] = result[j - gap]
                    j -= gap
                result[j] = temp
            gap //= 3
        return result
