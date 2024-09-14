# Majadas, Gio
# BSIT-SD 2A || CC 2103 - Data Structures and Algorithm

import time
import os

class SearchAlgo:
    def __init__(self):
        self.ARRAY_LIST = []
        
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
        return -1

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

    # 6. Merge Sort
    def mergeSort(self, array):
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

        return result

    # 7. Quick Sort
    def quickSort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        
        print(f"{self.quickSort(left)} {middle} {self.quickSort(right)}")

    def run(self):
        while True:
            os.system
            print(" -- Algorithm and Searching Program Menu -- ")
            print("1. Linear Search")
            print("2. Binary Search")
            print("3. Bubble Sort")
            print("4. Insertion Sort")
            print("5. Selection Sort")
            print("6. Merge Sort")
            print("7. Quick Sort")
            print("8. Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                self.createArray()
                self.linearSearch(self.ARRAY_LIST)
            elif choice == 2:
                self.createArray()
                self.binarySearch(self.ARRAY_LIST)
            elif choice == 3:
                self.createArray()
                self.bubbleSort()
            elif choice == 4:
                self.createArray()
                self.insertionSort()
            elif choice == 5:
                self.createArray()
                self.selectionSort()
            elif choice == 6:
                self.createArray()
                self.mergeSort(self.ARRAY_LIST)
            elif choice == 7:
                self.createArray()
                self.quickSort(self.ARRAY_LIST)
            elif choice == 8:
                print("Exiting...")
                time.sleep(2)
                break
            else:
                print("invalid choice. Please try again!")

if __name__ == "__main__":
    searching = SearchAlgo()
    searching.run()