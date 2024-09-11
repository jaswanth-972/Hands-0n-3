from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
    - arr: List of integers to be sorted.
    
    Returns:
    - Sorted list of integers.
    """
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves and return
    return merge(left_sorted, right_sorted)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
    - left: First sorted list.
    - right: Second sorted list.
    
    Returns:
    - Merged sorted list containing all elements from `left` and `right`.
    """
    merged = []
    left_index, right_index = 0, 0

    # Merge the two halves in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Testing the merge sort on a sample array
if __name__ == "__main__":
    array = [5, 2, 4, 7, 1, 3, 2, 6]
    sorted_array = merge_sort(array)
    print(f"Sorted array: {sorted_array}")
