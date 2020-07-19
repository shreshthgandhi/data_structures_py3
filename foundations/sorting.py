

def insertion_sort_recursive(array: list) -> list:
    if len(array) == 1:
        return array
    else:
        sorted_array = insertion_sort_recursive(array[:-1])
        element_to_insert = array[-1]
        for idx in reversed(range(len(sorted_array)+1)):
            if sorted_array[idx-1] <= element_to_insert:
                break
        sorted_array.insert(idx, element_to_insert)
        return sorted_array


def insertion_sort_iterative(array: list) -> list:
    for outer_idx in range(1, len(array)):
        element_to_insert = array[outer_idx]
        idx = outer_idx
        while idx >= 0 and array[idx-1] > element_to_insert:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = element_to_insert
    return array


print(insertion_sort_recursive([10, 9, 9, 9, 8, 8, 8]))
print(insertion_sort_iterative([10, 9, 9, 9, 8, 8, 8]))