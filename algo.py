from mainUI import *
import time

def bubbleSort(A,screen):
    l = len(A)
    for i in range(l):
        for j in range(0,l-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                drawBar(screen,A,True, {j:GREEN, j+1:RED})


def insertionSort(A,screen):
    l = len(A)
    for i in range(1,l):
        key = A[i]
        j=i-1
        drawBar(screen,A,True, {i:GREEN, i+1:RED})
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        time.sleep(0.05)
        

def partition(A, low, high,screen):
    i = (low-1)
    pivot = A[high]
    for j in range(low,high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    drawBar(screen,A,True, {low:GREEN, high:RED})
    time.sleep(0.05)
    return (i+1)
      
def quickSort(A, low, high,screen):
    if len(A) == 1:
        return A
    if low < high:
        pi = partition(A,low,high,screen)
        quickSort(A,low,pi-1,screen)
        quickSort(A,pi+1,high,screen)
        

def heapify(A, n, i, screen):
    largest = i
    l = 2 * i + 1    
    r = 2 * i + 2   
    if l < n and A[largest] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        drawBar(screen,A,True, {i:GREEN, largest:RED})
        time.sleep(0.01)
        heapify(A, n, largest,screen)

 
 
def heapSort(A,screen):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i, screen)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        drawBar(screen,A,True, {i:GREEN, 0:RED})
        time.sleep(0.01)
        heapify(A, i, 0, screen)