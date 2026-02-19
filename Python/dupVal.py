# def dup(arr):
#     seen = set()
#     dup = set()
#     for item in arr:
#         if item in seen:
#             dup.add(item)
#         else:
#             seen.add(item)
#     return list(dup)
# print(dup([1,1,2,3,4,5,5]))

arr = [1,2,3,3,4,4]
dict = {}
for a in arr:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1
for k, v in dict.items():
    if v > 1:
        print(k)