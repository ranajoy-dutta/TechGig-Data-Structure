'''
Second to smaller and larger
You will be given an array and you need to find the second largest and second smallest numbers and add them. 

Input Format
You will be taking a number as an input from stdin which tells about the length of the array. On another line, array elements should be there with single space between them. 
Output Format
You need to print the addition of second largest and second smallest elements to the stdout. 

Sample TestCase 1
Input
4
21 41 1 2
Output
23
'''

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    arr2=arr
    minn = min(arr)
    maxx = max(arr)
    arr.remove(minn)
    arr2.remove(maxx)
    minn = min(arr)
    maxx = max(arr2)
    print(minn+maxx)
    

main()

'''

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    pos = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i] += arr[j]
                arr[j] = arr[i]-arr[j] 
                arr[i] = arr[i]-arr[j]
    print(arr[1]+arr[n-2])
main()

'''