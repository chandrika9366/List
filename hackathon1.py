# Q1. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.The overall run time complexity should be O(log (m+n)).
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
num1=[1,3]
num2=[2]
i=0
while i<len(num1):
        list=num1+num2
        list.sort()
        sum=0
        j=0
        while j<len(list):
            sum+=list[j]
            j+=1
        i+=1
median=sum/len(list)
print(median)                  