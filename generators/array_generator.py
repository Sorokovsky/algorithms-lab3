from random import randint


def generate_array(variant: int = 11, minimum: int = 10, maximum: int = 1000) -> list[int]:
    count = (maximum - variant * minimum) * 20
    return [randint(minimum, maximum) for _ in range(count)]
