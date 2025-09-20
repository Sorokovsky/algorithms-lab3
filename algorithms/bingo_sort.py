from typing import Callable

from algorithms.base import SortingAlgorithm


class BingoSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Бінго сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        right = len(result) - 1
        while right > 0:
            current_index = 0
            indices = [0]  # Зберігаємо індекси кандидатів на максимум
            for index in range(1, right + 1):
                self._increment_iteration()
                if is_order_correct(result[index], result[current_index]):
                    current_index = index
                    indices = [index]
                elif result[index] == result[current_index]:
                    indices.append(index)
            # Переміщуємо всі входження максимального значення
            for index in reversed(indices):
                if index <= right:
                    result = self._swap(result, index, right)
                    right -= 1
        return result
