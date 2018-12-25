'''
Count negative numbers 
For this challenge, you will be given an array and you are asked to count how many numbers are negative. 

Input Format
You will be taking a number as an input from stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
Print the count to the stdout.

Sample TestCase 1
Input
7
-8 -7 6 0 7 1 6
Output
2
'''

def main():
    input()
    count=0
    arr = list(map(int,input().split()))
    for i in arr:
        if i<0:
           count += 1
    print(count)
main()

