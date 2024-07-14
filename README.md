# Big O Notation Exercise

## Analysis, Explanations & Optimizations

### ***LINEAR SEARCH***

#### Analysis

Linear search has a time complexity of ***O(n)***. While this is not the most efficient level of time complexity, it is relatively efficient, as in the worst-case scenario every element in the iterable must be traversed once before a result is returned.

#### Explanation

The simplest way to implement linear search on a list is to use the 'index' method. I used the 'not in' key words to cover the edge case in which the target is not included in the input array, in which case the function would return '-1'. Otherwise, the function returns the index of the target within the input array by calling the index method on the input array.

#### Optimizations

The implementation I did originally actually had a time complexity of ***O(2n)*** due to the unneccessary use of 'not in'. This caused the entire array to be traversed once to check for the existence of the target, then the calling of the 'index' method triggered a second traversal. TO optimize, I eliminated the use of 'not in', instead checking each element against the target, and then returning -1 in the event that none of the elements matched the target. This ensures that the array is only traversed one time (in the worst case where the target is the last element or the target does not exist in the array). I also improved the time efficiency slightly by using the enumerate function instead of the index method, but this is only a fractional improvement.

### ***BUBBLE SORT***

#### Analysis

Bubble sort is not an efficient method for sorting an unsorted list. In the worst case scenario in which the array is in reverse order, the time complexity of bubble sort is ***O(n<sup>2</sup>)***. The best case time complexity is ***O(n)***, which occurs when the list is already sorted. The average case is ***O(n<sup>2</sup>)*** as there is no foreknowledge about the sorting of the elements in the array. 

#### Explanation

The simplest way to implement bubble sort on a list is to use the a nested loop. The outer loop ensures all elements in the array will be traversed, and the inner loop tests each pair of elements to see if the element at index 'j' is greater than the element at index 'j + 1', and if not it swaps their positions in the array. At the conclusion of the nested loop, the now-sorted array is returned.

#### Optimizations

Similar to linear search, there is only a limited amount of optimization that can be done while still using bubble sort (vs. some other sorting algorithm). The only optimization that can be done is to include a flag, initialized with the value 'False', that tracks whether a given pair of elements are swapped during a given iteration of the inner loop. If they are, the flag is set to True, and the loop continues. When the loop reaches the end of the list without any swaps, the second if condition is triggered and the loop breaks. This prevents another unnecessary traversal of the list after it is already fully sorted. This provides a small degree of improvement in the time complexity of the bubble sort algorithm.