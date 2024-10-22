# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

from random import randint
import sys

# Aumentar el límite de recursión (Ej.: 10,000)
sys.setrecursionlimit(10000000)

# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


import time

def medirTiempoQuicksort(array):
    
    size = len(array)
    start=time.time()
    quickSort(array, 0, size - 1)
    end=time.time()
    executionTime=end-start
    return executionTime


def calcularPromedioQuickSort():

    listaPromedios=[]
    promedio=0
    for i in range(10):
        array=[randint(0,1000) for i in range(5000)]
        tiempo=medirTiempoQuicksort(array)
        listaPromedios.append(tiempo)
    
    for _ in range(len(listaPromedios)):
        promedio+=listaPromedios[_]
    
    print(f'tiempo promedio: {promedio/len(listaPromedios)}')

calcularPromedioQuickSort()


import random
import time

def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def medirTiempoBubblesort(array):
    
    start=time.time()
    bubble_sort(array)
    end=time.time()
    executionTime=end-start
    return executionTime



def CalcularPromedioBubbleSort ():
    listaPromedio=[]
    promedio=0
    for i in range(10):
        arr=[random.randint(0, 1000) for i in range (1000)]
        tiempo=medirTiempoBubblesort(arr)
        listaPromedio.append(tiempo)
    
    for _ in range(len(listaPromedio)):
        promedio+=listaPromedio[_]

    print(f'tiempo promedio: {promedio/len(listaPromedio)}')
CalcularPromedioBubbleSort()