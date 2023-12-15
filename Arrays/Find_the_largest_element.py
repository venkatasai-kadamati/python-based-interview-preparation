from typing import List

def sortArr(nums: List[int]) -> int:
    print("calling sortArr")
    nums.sort()
    return nums[-1]
    # end = nums[-1] || nums[len(nums)-1]

def findLargest(nums: List[int])-> int:
    print("calling findLargest")
    max = nums[0]
    for num in nums:
        if num > max: 
            max = num
    return max


if __name__ == "__main__":
    arr1 = [2, 50, 1, 3, 0]
    # arr2 = [8, 100, 5, 7, 9]
    # print("The Largest element in the array is:", sortArr(arr1))
    # print("The Largest element in the array is:", sortArr(arr2))
    
    # print("The Largest element in the array is:", findLargest(arr1))
    # print("The Largest element in the array is:", findLargest(arr2))

# Logic 
# 1. Sort the array in ascending order and return the last element of the array -> O(nlogn)
# 2. Find the largest element in the array by traversing the array -> O(n)