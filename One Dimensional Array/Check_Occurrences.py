'''
Check Occurrences
You will be given an array and you need to find the whether there is any element occurring thrice. If yes, then print 'True' else print 'False' 

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 
Output Format
You need to print the Boolean value. 

Sample TestCase 1
Input
5
10 13 13 27 13
Output
True
'''
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        flag=0
        for j in range(i+1,n):
            if arr[i]==arr[j] and flag==1:
                print('True')
                return 0
            elif arr[i]==arr[j]:
                flag+=1
    print('False')
main()

