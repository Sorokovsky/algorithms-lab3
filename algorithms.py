def sort_insert_descending(array: list) -> list:
    result = [item for item in array]
    iterations = 0
    for i in range(len(result) - 1):
        item = result[i]
        j = i
        while j > 0 and result[j - 1] < item:
            result[j] = result[j - 1]
            j = j - 1
            iterations += 1
        result[j] = item
    print("Кількість ітерацій за алгоритмом вставки по спаданню", iterations, sep=": ")
    return result


def sort_bingo_increasing(array: list) -> list:
    result = [item for item in array]
    iterations = 0
    minimum_index = get_minimum_index(result)
    iterations += len(result)
    result = swap_items(result, minimum_index, 0)
    print("Кількість ітерацій за алгоритмом вставки по спаданню", iterations, sep=": ")
    return result

def get_minimum_index(array: list) -> int:
    minimum_index = 0
    for i in range(len(array)):
        if array[i] < array[minimum_index]:
            minimum_index = i
    return minimum_index

def swap_items(array: list, first_index: int, second_index: int) -> list:
    result = [item for item in array]
    temp = result[first_index]
    result[first_index] = result[second_index]
    result[second_index] = temp
    return result