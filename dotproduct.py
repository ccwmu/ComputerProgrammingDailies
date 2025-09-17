import math

matrix1 = [[1, 2, 3],
           [4, 5, 6]
]

matrix2 = [[7,  8], 
           [9,  10],
           [11, 12]]

def dot_product(mat1, mat2):
    if len(mat1) != len(mat2[0]):
        raise ValueError("one matrix column must be equal to the other matrix row")

    result = []

    for i in range(len(mat1)):
        result_row = []
        for j in range(len(mat1)):
            num = 0
            for k in range(len(mat1[0])):
                num += mat1[i][j] * mat2[j][i]
            result_row.append(num)
        result.append(result_row)
    return result
            
            
dotproduct = dot_product(matrix1, matrix2)

for row in dotproduct:
    print(row)