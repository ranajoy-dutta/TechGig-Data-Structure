'''
Print Even
Given a 2D array, print the even numbers of it.

Input Format
You will taking two integers as input on one line separated by space representing rows and columns of the matrix. Following lines after that will be elements of the matrix with each element separated by space.

Constraints
1 <= n,m <= 1000

Output Format
Print the even elements of the matrix with each element separated by space.

Sample TestCase 1
Input
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Output
2 4 6 8 10 12 14 16
'''

def main():
    rows, cols = (list(map(int, input().split())))
    arr_even_nums = []
    for row in range(rows):
        elements = list(map(int, input().split()))
        for col in range(cols):
            if elements[col]%2==0:
                arr_even_nums.append(elements[col])
    print(*arr_even_nums)

main()