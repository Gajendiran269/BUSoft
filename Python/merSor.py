arr1 = [1,2,3]
arr2 = [1,5,6]
arr3 = sorted(arr1 + arr2)

def merge_sorted(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:   
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

arr3 = merge_sorted(sorted(arr1), sorted(arr2))
print(arr3)
# arr3 = arr1 + arr2
# print(arr3)
