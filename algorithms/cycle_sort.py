from typing import Callable

from algorithms.base import SortingAlgorithm


class CycleSort(SortingAlgorithm):
    def get_name(self) -> str:
        return "Циклічне сортування"

    def _sort(self, array: list[int], is_order_correct: Callable[[int, int], bool]) -> list[int]:
        result = array.copy()
        count = len(result)
        if count <= 1 or all(is_order_correct(result[i + 1], result[i]) for i in range(count - 1)):
            return result
        for cycle_start in range(count - 1):
            item = result[cycle_start]
            position = cycle_start
            for index in range(cycle_start + 1, count):
                self._increment_iteration()
                if is_order_correct(item, result[index]):
                    position += 1
            if position == cycle_start:
                continue
            while position < count and item == result[position]:
                self._increment_iteration()
                position += 1
            if position >= count:
                continue
            result[position], item = item, result[position]
            swap_count = 0
            max_swaps = count * 2
            visited = {cycle_start}
            while position != cycle_start:
                swap_count += 1
                if swap_count > max_swaps:
                    raise RuntimeError(
                        f"Infinite loop detected at cycle_start={cycle_start}, item={item}, array={result[:10]}...")
                if position in visited:
                    break
                visited.add(position)
                position = cycle_start
                for index in range(cycle_start + 1, count):
                    self._increment_iteration()
                    if is_order_correct(item, result[index]):
                        position += 1

                while position < count and item == result[position]:
                    self._increment_iteration()
                    position += 1
                if position >= count:
                    break
                result[position], item = item, result[position]
        return result
