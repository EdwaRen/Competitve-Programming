#Exercise1

def add(m):
    ''' (list) -> none
        Precondition: m is a m x n array
        change the array elements by adding 1
    '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            m[row][col] += 1

def add_V2(m):
    ''' (list) -> list
        Precondition: m is a m x n array
        The result is a new n x m array
    '''
    m1 = []
    for row in range(len(m)):
        m1.append([])
        for col in range(len(m[row])):
            m1[row].append(m[row][col]+1)
    return m1

def main():
    print("Enter the array elements with spaces between columns.")
    print("A row per line, and an empty line at the end.")

    matrix = []
    while True:
        line = input()
        if not line: break
        matrix.append(line)

    newMatrix = []
    for count in range(len(matrix)):
        newMatrix.append([int(i) for i in matrix[count].split(' ')])

    print("The array is: ")
    print(newMatrix)
    add(newMatrix)
    print("After executing the function add, the array is: ")
    print(newMatrix)
    print("with a new array created with add_V2: ")   
    matrix1 = add_V2(newMatrix)
    print(matrix1)
    print("After executing the function add_V2, the initial arrray is: ")
    print(newMatrix)

main()