'''
Find the element that appears once 
Given an array where every element occurs multiple times, except one element which occurs only once. Find the element that occurs once. 

Input Format
You will be taking a number as an input from stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
You need to print the number to the stdout.

Sample TestCase 1
Input
10
12 1 12 3 12 1 1 2 3 3
Output
2
'''
def main():
    n = int(input())
    arr = list(map(str,input().split()))
    mydict = dict()
    for i in arr:
        num = str(i)
        if num in mydict:
            count = mydict.get(num)
            mydict.update({num:count+1})
        else:
            mydict.update({num:1})
    print(*[val for val in mydict if mydict.get(val) == 1])

main()

