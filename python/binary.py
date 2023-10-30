n = int(input("Enter the number of elements in an array: "))
arr = []
print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))
item = int(input("Enter an element you want to search: "))
low = 0
high = n - 1
result=0
mid=0
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == item:
        print("Element found at location ",mid)
        result =1
        break
    elif arr[mid] > item:
        high = mid - 1
    else:
        low = mid + 1
  
else:
   print("Element not found at any location ")
stribg="alisha-12200"
print(stribg.split("-")[0])
