
"""
Q1) Write a function that can add any number of iterables when passed as parameters to it. 
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
Q2)Given a sequence of n values x1, x2,....xn and a window size k>0, the k-th moving average 
of the given sequence is defined as follows:

The moving avg sequence has n-k+1 elements as shown below. The moving avgs with k = 4 of a
ten-value sequence (n=10) is shown below:

Input : 10 20 30 40 50 60 70 80 90 100

Ans : 25 35 45 55 65 75 85

) Test a program for the same over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] for window size 3
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
        
movAvg(nums1, k); 
    
"""
Q3) Accept an 1-D array from user. Write a function to convert it into a matrix called Vandermonde
matrix. It is obtained as follows:

Each ith column of matrix is obtrained by raising the element of array to power i and maximum 
value of power dictates the number of columns in matrix. Also it is one of the parameters to 
the function generating the matrix. Another parameter to the function will be Boolean variable
'ascending'.

If ascending is true, power of the element will be in increasing order stating from 0. If ascending
is not specified the ith column of the matrix will be (p-i-1) where p is the number of columns.
Ex - M = [1,2,3]

1 1 1       (when p = 3 and ascending = True)
1 2 4
1 3 9

1 1 1       (when p = 3 and ascending = False)
4 2 1
9 1 3
""" 
    