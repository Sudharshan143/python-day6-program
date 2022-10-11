arr=[85,45,65,75,95]
arr1 =sorted(arr, reverse=True)
arr2 =sorted(arr, reverse=False)
k=int(input("M= "))
l=int(input("N= "))
print ("Mth maximum number= ", arr1[k-1])
print ("Nth minimum number= ", arr2[l-1])
