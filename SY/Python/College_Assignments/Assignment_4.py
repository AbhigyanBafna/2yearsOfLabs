
"""
Write a function that can add any number of iterables when passed as parameters to it. 
Include appropriate docstring for thee function. Show execution with various cases.
"""

def adder(nums):
#Adds custom amount of numbers.
    ans = 0
    for num in nums:
        ans += num
    print(ans)
   
   
n = int(input("Please enter no of elements : "))
nums = []
for i in range(n):
    no = int(input("Please enter element, :"))
    nums.append(no);
    
adder(nums)

"""
Given a sequence of n values x1, x2,....xn and a window size k>0, the k-th moving average 
of the given sequence is defined as follows:

The moving avg sequence has n-k+1 elements as shown below. The moving avgs with k = 4 of a
ten-value sequence (n=10_ is shown below:

1 2 3 4 5 6 7 8 9 10
"""

k = int(input("Enter Window Size(k) : "))
nums1 = []
n = int(input("Please enter no of elements : "))
for i in range(n):
    no = int(input("Enter Element :"))
    nums1.append(no);

def movAvg(nums, k):
    n = len(nums)
    no = n-k+1
    ans = 0
    for i in range(no):
            ans = sum(nums[i:i+k])
            print(ans/k)
            ans=0
        
movAvg(nums1, k)
            
    
    
    