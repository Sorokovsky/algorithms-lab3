from algorithms.bingo_sort import BingoSort
from algorithms.comb_sort import CombSort
from algorithms.insertion_sort import InsertionSort
from analysers.sorting_algorithms_analyzer import SortingAlgorithmsAnalyzer
from comparators.descending_comparator import is_descending
from comparators.increese_compararor import is_increasing
from generators.array_generator import generate_array


def main():
    array = generate_array()
    analyzer = SortingAlgorithmsAnalyzer()
    analyzer.add_algorithm(InsertionSort(), is_descending)
    analyzer.add_algorithm(BingoSort(), is_increasing)
    analyzer.add_algorithm(CombSort(), is_descending)
    analyzer.run(array)
    analyzer.print_statistics()
    analyzer.show_statistics_in_histograms()
if __name__ == '__main__':
    main()