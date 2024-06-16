Write a Python program to sort a list of elements using the merge sort algorithm.

For example:

Input	Result
5
6 5 4 3 8
3 4 5 6 8
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    n = int(input())
    elements = list(map(int, input().split()))

    merge_sort(elements)
    
    print(" ".join(map(str, elements)))

main()
Input	Expected	Got	
5
6 5 4 3 8
3 4 5 6 8
3 4 5 6 8
9
14 46 43 27 57 41 45 21 70
14 21 27 41 43 45 46 57 70
14 21 27 41 43 45 46 57 70
4
86 43 23 49
23 43 49 86
23 43 49 86
