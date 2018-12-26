'''
Leader
Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.  

Input Format
You will take an integer as input from STDIN which represent the length of the array and on another line array elements will be there separated by single space. 
Output Format
print the numbers one on each line to the STDOUT. 

Sample TestCase 1
Input
6
16 17 4 3 5 2
Output
17
5
2
'''

def main():
    n = int(input())-1
    arr = list(map(int,input().split()))
    maxx,arr2 = arr[n],[]
    arr2.append(maxx)
    while n>=0:
        if arr[n]>maxx:
            arr2.append(arr[n])
            maxx = arr[n]
        n-=1
    print(*arr2[::-1],sep='\n')
    
    return 0

main()

