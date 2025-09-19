from algorithms.insertion_sort import InsertionSort


def is_descending(first: int, second: int) -> bool:
    return first < second

def main():
    array = [3, 2, 1, 5, 4]
    print(array)
    algorithm = InsertionSort()

    result = algorithm.sort(array, is_descending)
    print(result)

if __name__ == '__main__':
    main()