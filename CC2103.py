# Majadas, Gio
# BSIT-SD 2A || CC 2103 - Data Structures and Algorithm

# For aesthetic purposes only heheh
import time
import os

class SearchAlgo:
    def __init__(self):
        self.ARRAY_LIST = []

    # Need for other functions, to ask the user how many elements in an array to be stored
    def createArray(self):
        size = int(input("Enter the size of the array: "))
        self.ARRAY_LIST = [int(input(f"Enter element {i+1}: ")) for i in range(size)]

    # 1. Linear Search
    def linearSearch(self, target):
        target = int(input("Enter the element to search : "))
        for i, element in enumerate(self.ARRAY_LIST):
            if element == target:
                print(f"The index number is : {i}, and the element is : {target} | LINEAR SEARCH")
                time.sleep(2)
                return
        print("Element not found")
        time.sleep(2)

    # 2. Binary Search
    def binarySearch(self, target):
        target = int(input("Enter the element to search : "))
        low, high = 0, len(self.ARRAY_LIST) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.ARRAY_LIST[mid] == target:
                print(f"The index number is : {mid}, and the element is : {target} | BINARY SEARCH")
                time.sleep(2)
                return mid
            elif self.ARRAY_LIST[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print("Element not found")
        time.sleep(2)

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

    # 4. Insertion Sort
    def insertionSort(self):
        n = len(self.ARRAY_LIST)
        for i in range(1, n):
            key = self.ARRAY_LIST[i]
            j = i - 1
            while j >= 0 and key < self.ARRAY_LIST[j]:
                self.ARRAY_LIST[j + 1] = self.ARRAY_LIST[j]
                j -= 1
            self.ARRAY_LIST[j + 1] = key
        print(f"Sorted Array : {self.ARRAY_LIST}")
        input("Press Enter to continue...")

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

    # 6. Quick Sort
    def quickSort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        
        print(f"{self.quickSort(left)} {middle} {self.quickSort(right)}")
        input("Press Enter to continue...")

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
            rightElements = result[middle:]
            if len(result) % 2 == 0:
                print(f"Left Element(s) : {leftElements}")
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
            # os.system("cls")
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
                self.quickSort(self.ARRAY_LIST)
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
                print("Invalid choice. Please try again!")
                os.system("cls")

if __name__ == "__main__":
    searching = SearchAlgo()
    searching.run()