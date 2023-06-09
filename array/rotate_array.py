'''
Rotate the array A by B positions.

So, for example,


A : [1 2 3 4 5 6]
B : 1

The output :

[2 3 4 5 6 1]
'''


def rotate_array(a: list, b: int) -> list:
    result = []
    for i in range(len(a)):
        result.append(a[(i + b) % len(a)])

    return result


if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    B = 100
    print(rotate_array(A, B))
