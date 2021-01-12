Algorithm:
- Traverse both trees with preorder (this will result in two arrays)
- Convert the second array to a set
- Iterate over the first array and check if the element exists in the set
    - If exists add to the output set


Pseudo Code:
Define a function treesIntersection(T1, T2)
    // Input: Two trees
    // Output: Set of common values between the two trees
    Declare array1 <- T1.preorder()     // O(n)
    Declare array2 <- T2.preorder()     // O(n)
    Declare set2 <- Set of array2       // O(n)
    Declare outputSet <- Empty set      // O(1)
    For element in array1               // O(n)
        If element is in set2 then, // O(1)
            add it to the outputSet  // O(1)
    Return outputSet        // O(1)


O(n) for time
O(n) for space

Cases:
//    Same size
//    Different size
1.    Empty (one or two):
        Start with the smaller one
//    Intersection
//    No Intersection



Code:
...
...
...



def fun(ll):
    // ll.__str__()       "head -> 3 -> 7 -> 8 -> None"
    1. Your interviewer doesn't know what it means
    2. You can't call it this way, it's called when you print only

