def main():
    # get input from user and split it's chars to n & m
    n, m = map(int, input().split())
    # creat a matrix with n row and m cols
    matrix = create_matrix(n, m)
    # creat a matrix with m row and n cols (trasnspose matrix)
    transpose_matrix = list(zip(*matrix))
    # count the walls in matrix
    row_walls = build_wall(matrix)
    # count the walls in transpose_matrix (if exists)
    column_walls = build_wall(transpose_matrix) if transpose_matrix else 0
    # the amount of walls needed to stop the virus
    print(row_walls + column_walls)
    
def create_matrix(n: int, m: int) -> list:
    """
    This function create a matrix and check inputs should be valid
    """
    matrix = []
    for i in range(n):
        row_str = input().lstrip()
        row = [int(num) for num in row_str.split()]
        if len(row) != m:
            continue
        matrix.append(row)
    return matrix

def build_wall(matrix: list) -> int:
    """
    This function counts the walls in row between 0 & 1 in a matrix
    """
    count = 0
    for row in matrix:
        for index, _ in enumerate(row):
            if index == len(row) - 1:
                continue
            if row[index] != row[index + 1]:
                count = count + 1
    return count
if __name__ == '__main__':
    main()
