# create shuffle(arr), to efficiently shuffle a given array’s values.
import random
def shuffle(arr):
    for i in range(len(arr) -1,0,-1):
        j = random.randint(0,i)
        arr[i],arr[j]= arr[j],arr[i]

my_array = [1,2,3,4,5]
shuffle(my_array)
print(my_array)

# Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: 
# first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. 
# Return array containing heights of buildings you can see, 
# in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().
def visible_buildings(buildings):
    visible = []
    max_height = 0
    for height in buildings:
        if height > max_height:
            visible.append(height)
            max_height = height
    return visible
print(visible_buildings([-1,1,1,7,3]))

# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. 
# Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100]
def combine_arrays(arr1, arr2):
    combine = []
    i ,j =0, 0
    while i< len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            combine.append(arr1[i])
            i += 1
        else:
            combine.append(arr2[j])
            j += 1
    combine += arr1[i:] + arr2[j:]
    return combine

arr1 = [4,15,100]
arr2 = [10,20,30,40]
results = combine_arrays(arr1,arr2)
print(results)

# The Luhn formula is sometimes used to validate credit card numbers. 
# Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on the card), 
# and returns a boolean whether the card digits satisfy the Luhn formula, as follows:
#       Set aside the last digit; do not include it in these calculations (until step 5);
#       Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
#       If any results are larger than 9, subtract 9 from them;
#       Add all numbers (not just our odds) together;
#       Now add the last digit back in – the sum should be a multiple of 10.
def isCreditCardValid(digitArr):
    last_digit = digitArr.pop()
    for i in range(len(digitArr)-1,-1,-2):
        digitArr[i] *=2
        if digitArr[i] > 9:
            digitArr[i] -=9
    total = sum(digitArr)
    total += last_digit
    return total % 10==0

result = isCreditCardValid( [5,2,2,8,2])
print(result)
