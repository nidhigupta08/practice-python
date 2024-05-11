class SortAlgorithm:
    def sort(self, data):
        pass

class BubbleSort(SortAlgorithm):
    def sort(self, data):
        return sorted(data)

class QuickSort(SortAlgorithm):
    def sort(self, data):
        return sorted(data, reverse=True)

# Usage
bubble_sort = BubbleSort()
data = [5, 2, 7, 1, 9]
print("Sorted data using Bubble Sort:", bubble_sort.sort(data))

quick_sort = QuickSort()
print("Sorted data using Quick Sort:", quick_sort.sort(data))
