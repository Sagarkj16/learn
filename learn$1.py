#binary sorting
print("resource open")
nums=[1,2,7,6,5,4,33,3,5,6,7,77,665,3434,465,54535,657]
def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j



        else:
            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp

sort(nums)
print(nums)
print("resource closed")