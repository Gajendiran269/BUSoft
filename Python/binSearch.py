arr = [1,2,3,6,7]
tar = 3
l=0
found=False
r=len(arr)-1
while(l<=r):  
    mid = (l + r) // 2
    if arr[mid] == tar:
        found = True
        break
    elif tar < arr[mid]:
        r = mid - 1
    else:
        l = mid + 1
print("found") if found else print("not found")