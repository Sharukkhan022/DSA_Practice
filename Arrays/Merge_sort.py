def merge_sort(arr):
    # Base case: an array of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from both sub-arrays and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements from the left or right sub-array
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Example Usage:
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    
    sorted_data = merge_sort(data)
    print("Sorted array:  ", sorted_data)