'''
Even Gets Bigger
For this challenge, you will be given an array and you are asked to form a number with the help of even numbers available in the array. Actually, you need to form a number by appending even numbers in the array.In case you did not found any even number, print 0 to the stdout. 

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
Print the number that you will be forming with the even numbers to the stdout.

Sample TestCase 1
Input
6
22 21 47 34 78 91
Output
223478
'''

def main():
    input()
    arr = list(map(int,input().split()))
    num = ''
    for i in arr:
        if i%2 == 0:
            num += str(i)
    if len(num)==0:
        print(0)
        return 0
    print(int(num)) 
    
main()

