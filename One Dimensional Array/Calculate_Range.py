'''
calculate range
You will be given an array and you need to find the range. 

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
You need to print the range.

Sample TestCase 1
Input
6
90 98 100 102 105 110
Output
20
'''

def main():
    input()
    arr = list(map(int,input().split()))
    minn,maxx = arr[0],arr[0]
    for i in arr:
        if i<minn:
            minn = i
        elif i>maxx:
            maxx = i
            
    print(maxx-minn)
main()