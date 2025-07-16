# initialize myArray
myArray = [1,3,5,7,9,11,13,15,17]


i = 0
while i < len(myArray):
   print(myArray[i])
   i += 1 


def removeEnd(arr, length):
   if length > 0:
      arr[length - 1] = 0 
      
removeEnd(myArray, 9)

print(myArray)
def removeMiddle(arr, i, length):
   for index in range(i + 1, length):
      arr[index - 1] = arr[index]


removeMiddle(myArray, 2, 9)
print(myArray)