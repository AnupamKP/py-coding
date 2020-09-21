'''
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]

'''


def spiral_matrix(A: list) -> list:
    left, right = 0, len(A[0])
    top, bottom = 0, len(A)
    result = []

    while True:
        if left > right-1:
            break

        for top_el in range(left, right):
            result.append(A[top][top_el])
        top += 1

        if top > bottom-1:
            break

        for right_el in range(top, bottom):
            result.append(A[right_el][right-1])
        right -= 1

        if left > right-1:
            break

        for bottom_el in range(right-1, left-1, -1):
            result.append(A[bottom-1][bottom_el])
        bottom -= 1

        if top > bottom-1:
            break

        for left_el in range(bottom-1, top-1, -1):
            result.append(A[left_el][left])
        left += 1

    return result


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_matrix(A))
