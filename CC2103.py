# Majadas, Gio
# BSIT-SD 2A || CC 2103 - Data Structures and Algorithm

# For aesthetic purposes only heheh
import time
import os

ERROR = "\033[38;5;196m"
RESET = "\033[0m"

class SearchAlgo:
    def __init__(self):
        self.ARRAY_LIST = []

    def createArray(self):
        while True:
            try:
                size = int(input("Enter the size of the array: "))
                break
            except ValueError:
                print(f"{ERROR}Invalid input. Please enter a valid integer for the size of the array.{RESET}")
        for i in range(size):
            while True:
                try:
                    element = int(input(f"Enter element {i+1}: "))
                    self.ARRAY_LIST.append(element)
                    break
                except ValueError:
                    print(f"{ERROR}Invalid input. Please enter a valid integer for element {i+1}.{RESET}")

    # 1. Linear Search
    def linearSearch(self, target):
        target = int(input("Enter the element to search : "))
        for i, element in enumerate(self.ARRAY_LIST):
            if element == target:
                print(f"The index number is : {i}, and the element is : {target} | LINEAR SEARCH")
                input("Press Enter to continue...")
                return self.ARRAY_LIST
        print("Element not found")
        input("Press Enter to continue...")

    # 2. Binary Search
    def binarySearch(self, target):
        target = int(input("Enter the element to search : "))
        low, high = 0, len(self.ARRAY_LIST) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.ARRAY_LIST[mid] == target:
                print(f"The index number is : {mid}, and the element is : {target} | BINARY SEARCH")
                input("Press Enter to continue...")
                return self.ARRAY_LIST
            elif self.ARRAY_LIST[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print("Element not found")
        input("Press Enter to continue...")

    # 3. Bubble Sort
    def bubbleSort(self):
        n = len(self.ARRAY_LIST)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.ARRAY_LIST[j] > self.ARRAY_LIST[j + 1]:
                    self.ARRAY_LIST[j], self.ARRAY_LIST[j + 1] = self.ARRAY_LIST[j + 1], self.ARRAY_LIST[j]
                    swapped = True
            if not swapped:
                break
        print(f"Sorted Array : {self.ARRAY_LIST}")
        input("Press Enter to continue...")
        return self.ARRAY_LIST

    # 4. Insertion Sort
    def insertionSort(self):
        array = self.ARRAY_LIST[:]
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        self.ARRAY_LIST = array
        print(f"Sorted Array : {self.ARRAY_LIST}")
        input("Press Enter to continue...")
        return self.ARRAY_LIST

    # 5. Selection Sort
    def selectionSort(self):
        n = len(self.ARRAY_LIST)
        for i in range(n):
            minIndex = i
            for j in range(i + 1, n):
                if self.ARRAY_LIST[j] < self.ARRAY_LIST[minIndex]:
                    minIndex = j
            self.ARRAY_LIST[i], self.ARRAY_LIST[minIndex] = self.ARRAY_LIST[minIndex], self.ARRAY_LIST[i]
        print(f"Sorted Array : {self.ARRAY_LIST}")
        input("Press Enter to continue...")
        return self.ARRAY_LIST

    # 6. Quick Sort
    def quickSort(self, array, low, high):
        if low < high:
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            pivotIndex = i + 1
            self.quickSort(array, low, pivotIndex - 1)
            self.quickSort(array, pivotIndex + 1, high)
        if low == 0 and high == len(array) - 1:
            print(f"Sorted Array : {array}")
            input("Press Enter to continue...")
            return self.ARRAY_LIST

    # 7. Merge Sort
    def mergeSort(self, array):
        if array is None:
            array = self.ARRAY_LIST
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        if array == self.ARRAY_LIST:
            print(f"Sorted Array : {result}")
            middle = len(result) // 2
            leftElements = result[:middle]
            middleElement = result[middle]
            rightElements = result[middle + 1:]
            if len(result) % 2 == 0:
                print(f"Left Element(s) : {leftElements}")
                print("Middle Element: None")
                print(f"Right Element(s) : {rightElements}")
            else:
                print(f"Left Element(s) : {leftElements}")
                print(f"Middle Element : {middleElement}")
                print(f"Right Element(s) : {rightElements}")
            input("Press Enter to continue...")
        return result

    # Main Menu
    def run(self):
        while True:
            os.system("cls")
            print(" -- Algorithm and Searching Program Menu -- \n")
            print("\t1. Linear Search")
            print("\t2. Binary Search")
            print("\t3. Bubble Sort")
            print("\t4. Insertion Sort")
            print("\t5. Selection Sort")
            print("\t6. Quick Sort")
            print("\t7. Merge Sort")
            print("\t8. Exit")
            choice = int(input("\n\tEnter your choice : "))
            os.system("cls")
            self.ARRAY_LIST = []
            if choice == 1:
                print("\t-- Linear Search --\n")
                self.createArray()
                self.linearSearch(self.ARRAY_LIST)
            elif choice == 2:
                print("\t-- Binary Search --\n")
                self.createArray()
                self.binarySearch(self.ARRAY_LIST)
            elif choice == 3:
                print("\t-- Bubble Sort --\n")
                self.createArray()
                self.bubbleSort()
            elif choice == 4:
                print("\t-- Insertion Sort --\n")
                self.createArray()
                self.insertionSort()
            elif choice == 5:
                print("\t-- Selection Sort --\n")
                self.createArray()
                self.selectionSort()
            elif choice == 6:
                print("\t-- Quick Sort  --\n")
                self.createArray()
                self.quickSort(self.ARRAY_LIST, 0, len(self.ARRAY_LIST) - 1)
            elif choice == 7:
                print("\t-- Merge Sort --\n")
                self.createArray()
                self.mergeSort(self.ARRAY_LIST)
            elif choice == 8:
                # Exiting the program after a 2 second delay
                print("Exiting...")
                time.sleep(2)
                print("Goodbye!")
                break
            else:
                print(f"{ERROR}Invalid choice. Please try again!{RESET}")
                os.system("cls")
            os.system("cls")
            answer = str(input("\n\tDo you want to use the program again? (Y/N): "))
            while True:
                if answer.lower() == "y":
                    break
                elif answer.lower() == "n":
                    os.system("cls")
                    print("Exiting...")
                    time.sleep(2)
                    print("Goodbye!")
                    exit()
                else:
                    print(f"\n\t{ERROR}Invalid input. Please enter either Y or N.{RESET}")
                    answer = str(input("\n\tDo you want to use the program again? (Y/N): "))

if __name__ == "__main__":
    searching = SearchAlgo()
    searching.run()