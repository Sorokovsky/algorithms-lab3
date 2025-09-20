from typing import Callable

from algorithms.base import SortingAlgorithm


class CombSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Сортування гребінцем"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        gap = count
        is_swapped = False
        if gap < 2:
            return result
        while gap > 1 or is_swapped:
            gap = self._update_gap(gap)
            is_swapped = False
            for index in range(0, count - gap, gap):
                self._increment_iteration()
                if not is_order_correct(result[index], result[index + gap]):
                    result = self._swap(result, index, index + gap)
                    is_swapped = True
        return result

    @staticmethod
    def _update_gap(gap: int) -> int:
        gap = (gap * 10) / 13
        if gap == 9 or gap == 10:
            gap = 11
        return int(max(1, gap))
