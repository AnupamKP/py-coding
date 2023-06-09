'''
You are in an infinite 2D grid where you can move in any of the 8 directions.
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 

Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]


Example Output
Output 1:

 2

'''


def cover_min_steps(A: list, B: list) -> int:
    result = 0
    for i in range(len(A)-1):
        x1 = A[i]
        x2 = A[i+1]
        y1 = B[i]
        y2 = B[i+1]
        result += max((abs(x2-x1)), (abs(y2-y1)))

    return result


if __name__ == "__main__":
    A = [0, 1, 1]
    B = [0, 1, 2]
    print(cover_min_steps(A, B))
