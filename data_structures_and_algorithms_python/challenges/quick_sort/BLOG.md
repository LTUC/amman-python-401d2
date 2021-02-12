## Quick Sort
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

* Always pick first element as pivot.
* Always pick last element as pivot (implemented below)
* Pick a random element as pivot.
* Pick median as pivot.
* The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

## Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```        
## Trace
          ## [9,-3,5,2,6,8,-6,1,3]


![image](https://miro.medium.com/max/875/1*Njux2syraq38jzBvkNPbQg.png)
![image](https://miro.medium.com/max/875/1*q-8787kpdwT57YKVAacEEQ.png)
![image](https://miro.medium.com/max/875/1*hDJi4Rx7bzLVGtUKNGRyMA.png)
![image](https://miro.medium.com/max/875/1*3_3zrlr1daGA-8A1RMR6kw.png)
![image](https://miro.medium.com/max/875/1*S4fwEGRJJ__WLT7GcevQ-w.png)
![image](https://miro.medium.com/max/875/1*3q7OwlzKKN6WP1FsF5VC2g.png)
![image](https://miro.medium.com/max/875/1*mc7Y6XmggbtNIqpDCJ8TgQ.png)

## Efficency
Time-complexity: The worst-case complexity of quicksort is O(n2) as lots of comparisons are needed in the worst condition. Whereas in mergesort, worst-case and average-case have the same complexities O(n log n).
