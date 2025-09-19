import abc
from time import time
from typing import Callable


class SortingAlgorithm(abc.ABC):
    def __init__(self):
        self._iterations = 0
        self._start_time = time()
        self._end_time = time()

    def _clear_iterations(self) -> None:
        self._iterations = 0

    def _record_start_time(self) -> None:
        self._start_time = time()

    def _record_end_time(self) -> None:
        self._end_time = time()

    def _increment_iteration(self) -> None:
        self._iterations += 1

    def get_iterations_count(self) -> int:
        return self._iterations

    def get_processing_time(self) -> float:
        return self._end_time - self._start_time

    def sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        self._clear_iterations()
        self._record_start_time()
        result = self._sort(array, is_order_correct)
        self._record_end_time()
        return result

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        pass

    @staticmethod
    def _swap(array: list[int], first_index: int, second_index: int) -> list[int]:
        result = array.copy()
        temp = result[first_index]
        result[first_index] = result[second_index]
        result[second_index] = temp
        return result
