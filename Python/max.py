arr = [1,2,3,4,5]
max_ = float("-inf")
for i in range(len(arr)):
    if arr[i] > max_:
        max_ = arr[i]
print(max_)