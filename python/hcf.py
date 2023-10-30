n=int(input("Enter the number of elements you want sort "))
print("Enter ",n," elements")
arr=[]
for i in range(0,n):
    arr.append(int(input()))
for i in range(0,n):
   temp=arr[i]
   j=i-1
   while j>=0 and arr[j]> temp:
     arr[j+1]=arr[j]
     j=j-1
   arr[j+1]=temp
print("Sorted array is ")
for i in range (0,n):
  print(arr[i],end=" ")    
