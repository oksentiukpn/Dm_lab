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
            matrix = [list(line.strip('\n')) for line in file]
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

##############################################################
#
def relation_breakdown(matrix: list) -> list:
    '''
    a
    '''
    classes = []
    def add_to_classes(index: int, j_index: int, row: list, element: int):
        if classes == []:
            classes.append([index])
            if index != j_index:
                classes[0].append(j_index)
        for m, n in enumerate(classes):
            for o, p in enumerate(n):
                #print(f"{classes}")
                #print(f'{n=}, {p=}, {index=}, {j_index=}')
                if index == p or j_index == p:
                    break
            else:
                classes.append([index])
                if index != j_index:
                    classes[m].append(j_index)


    for index, row in enumerate(matrix):
        for j_index, element in enumerate(row):
            if element == 1:
                add_to_classes(index, j_index, row, element)

    #print(classes)

# matr = [
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]
# ]
##############################################################
if __name__ == "__main__":
    #relation_breakdown(matr)
    pass
