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

    # Append any remaining elements from left or right
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Testing the merge sort with diverse test cases
if __name__ == "__main__":
    test_cases = [
        [5, 2, 4, 7, 1, 3, 2, 6],  # Typical case
        [],  # Edge case: empty list
        [1],  # Edge case: single element
        [5, 4, 3, 2, 1],  # Reversed list
        [1, 1, 1, 1],  # List with all identical elements
        [-5, -2, -4, 0, 3, 2, 1],  # List with negative numbers
        [10, 20, 30, 40, 50]  # Already sorted list
    ]

    for i, array in enumerate(test_cases):
        sorted_array = merge_sort(array)
        print(f"Test case {i + 1}: {sorted_array}")
