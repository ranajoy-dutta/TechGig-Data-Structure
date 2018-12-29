'''
Second Largest 
For this challenge, you will be given an array and you are asked to find second largest number and second smallest number and multiply them. 

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 
Output Format
Print the multiplication to the STDOUT. 

Sample TestCase 1
Input
6
11 9 7 6 12 14
Output
84
'''

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i]+=arr[j]
                arr[j] = arr[i]-arr[j]
                arr[i] = arr[i]-arr[j]
    print(arr[1]*arr[-2]) 
main()

