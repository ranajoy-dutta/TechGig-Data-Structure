'''
Third Largest
You will be given an array and you need to find the third largest and print it to the stdout.

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.
Output Format
You need to print the third largest element to the stdout.

Sample TestCase 1
Input
7
25 26 7 8 10 11 79
Output
25
'''

def main(arr, exclude=[]):
    maxx=min(arr)
    for i in arr:
        if (i>maxx) and (i not in exclude):
            maxx = i
            print(i)
    exclude.append(maxx)
    print(exclude)
    if len(exclude)==3:
        return exclude[2]
    return main(arr,exclude)
    
int(input())
array = list(map(int,input().split()))
print(main(array))
