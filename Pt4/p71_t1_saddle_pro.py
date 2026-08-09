def saddle_point(matrix):
    m, n = len(matrix), len(matrix[0])
    row_min = [min(matrix[i]) for i in range(m)]        # O(m·n)
    col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]  # O(m·n)
    for i in range(m):
        for j in range(n):                              # O(m·n)
            if matrix[i][j] == row_min[i] == col_max[j]:
                print(f"马鞍点:({i},{j})")

#教材标准解法.