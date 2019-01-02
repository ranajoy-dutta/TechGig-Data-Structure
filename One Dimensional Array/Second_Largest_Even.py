'''
Second largest even 
For this challenge, you will be given an array and you are asked to find the second largest even number and print it to the stdout. 

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
Print the second largest even number to the stdout.

Sample TestCase 1
Input
6
78 92 44 63 71 97
Output
78
'''
def main():
    n =int(input())
    arr = list(map(int,input().split()))
    maxx=sec=min(arr)
    for i in range(n-1):
        if (arr[i] > maxx): 
            sec = maxx
            maxx = arr[i]
        elif (arr[i] > sec and arr[i] != maxx): 
            sec = arr[i] 
    print(sec)
main()