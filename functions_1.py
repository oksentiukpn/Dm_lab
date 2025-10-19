'''
Our lab
'''
##############################################################
# 1
def read_file(file: str) -> list | None:
    '''
    This function returns opened file in list type

    :param file: str, name of the file
    :return: list | None, matrix or None if invalid file
    '''
    try:
        with open(file, 'r', encoding='utf-8') as file:
            matrix = []
            for line in file:
                matrix.append(line.strip("\n"))
            for i, l in enumerate(matrix):
                matrix[i] = list(l)
            return matrix
    except FileNotFoundError:
        return None

def write_file(matrix: list) -> bool:
    '''
    This function write matrix in file

    :param matrix: list, matrix that we need to write to file
    :return: bool, True if everything is ok, and False if invalid file
    '''
    try:
        with open('result.csv', 'w', encoding='utf-8') as file:
            for i, l in enumerate(matrix): # i - index, l - letter
                for j, k in enumerate(l):
                    matrix[i][j] = str(k)
                file.write("".join(matrix[i]) + '\n')
    except FileNotFoundError:
        return False
    return True
##############################################################
