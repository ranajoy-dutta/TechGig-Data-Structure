'''
Find Biggest Difference 
You will be given an array and you need to find the biggest difference between any two numbers present in the array.

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
You need to print the biggest difference between any two numbers present in the array.

Sample TestCase 1
Input
7
29 79 72 81 9 7 21
Output
74
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