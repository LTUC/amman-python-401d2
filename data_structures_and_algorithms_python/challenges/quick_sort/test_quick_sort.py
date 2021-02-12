from quick_sort import QuickSort



def test_quick_sort():
    actual = QuickSort(arr = [2,4,5,3,8],left = 0,right = len([2,3,4,5,8])-1)
    expected = [2,3,4,5,8]
    assert actual == expected

def test_quick_sort_negative():
    actual = QuickSort(arr = [2,-4,5,3,8],left = 0,right = len([-4,2,3,5,8])-1)
    expected = [-4,2,3,5,8]
    assert actual == expected    

def test_quick_sort_duplicated_number():
    actual = QuickSort(arr = [2,5,5,3,5],left = 0,right = len([2,5,5,3,5])-1)
    expected = [2,3,5,5,5]
    assert actual == expected   

def test_quick_sort_sorted():
    actual = QuickSort(arr = [2,5,7,9,12],left = 0,right = len([2,5,7,9,12])-1)
    expected = [2,5,7,9,12]
    assert actual == expected 

def test_quick_sort_sortedd_reverse():
    actual = QuickSort(arr = [12,9,7,5,2],left = 0,right = len([12,9,7,5,2])-1)
    expected = [2,5,7,9,12]
    assert actual == expected       
    