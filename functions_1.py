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
    Break down a equivalent relation matrix into equivalence classes.

    The input matrix represents a relation `R` on a finite set of elements
    {0, 1, ..., n-1}, where `matrix[i][j] == 1` means "element i is related to element j".

    This function finds all equivalence classes — groups of elements that are
    mutually related (directly or through a chain of relations).

    :param matrix: list, our equivalent matrix
    :return: list, equivalent classes
    >>> relation_breakdown([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    [[0, 1], [2]]
    >>> relation_breakdown([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [[0], [1], [2]]
    >>> relation_breakdown([[1, 1, 1],
    ...                     [1, 1, 1],
    ...                     [1, 1, 1]])
    [[0, 1, 2]]
    >>> relation_breakdown([[1, 0, 0, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 0, 0, 1]])
    [[0], [1, 2], [3]]
    >>> relation_breakdown([[1, 1, 0, 0],
    ...                     [1, 1, 1, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 0, 0, 1]])
    [[0, 1, 2], [3]]
    >>> big_matrix = [
    ... [1,1,0,0,0,0,0,0,0,0],
    ... [1,1,0,0,0,0,0,0,0,0],
    ... [0,0,1,1,1,0,0,0,0,0],
    ... [0,0,1,1,1,0,0,0,0,0],
    ... [0,0,1,1,1,0,0,0,0,0],
    ... [0,0,0,0,0,1,1,0,0,0],
    ... [0,0,0,0,0,1,1,0,0,0],
    ... [0,0,0,0,0,0,0,1,1,1],
    ... [0,0,0,0,0,0,0,1,1,1],
    ... [0,0,0,0,0,0,0,1,1,1]
    ... ]
    >>> relation_breakdown(big_matrix)
    [[0, 1], [2, 3, 4], [5, 6], [7, 8, 9]]
    '''
    classes = []
    def add_to_classes(index: int, j_index: int):
        if not classes:
            classes.append([index])
        for i, m in enumerate(classes): # check for existance in classes
            if index in m and j_index in m:
                continue
            elif index in m and j_index not in m:
                classes[i].append(j_index)
                break
            elif index not in m and j_index in m:
                classes[i].append(index)
                break
            else:
                if i + 1 == len(classes):
                    if index != j_index:
                        classes.append([j_index, index])
                    else:
                        classes.append([index])
                    break
                else:
                    continue

    for index, row in enumerate(matrix):
        for j_index, element in enumerate(row):
            if element == 1:
                add_to_classes(index, j_index)
    return classes

#############################################################
# 5
def is_transitive(matrix: list) -> bool:
    '''
    Checks if relation is transitive

    A relation R is transitive if for all i, j, k:
    (i,j) ∈ R and (j,k) ∈ R ⇒ (i,k) ∈ R

    :param matrix: list, relation matrix
    :return: bool, True or False
    >>> M = [
    ...     [1, 1, 0],
    ...     [0, 1, 1],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M)
    False

    >>> M2 = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M2)
    True

    >>> M3 = [
    ...     [1, 0, 0],
    ...     [0, 1, 0],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M3)
    True

    >>> M_big = [
    ... [1,1,1,0,0,0,0,0,0,0],
    ... [0,1,1,1,0,0,0,0,0,0],
    ... [0,0,1,1,1,0,0,0,0,0],
    ... [0,0,0,1,1,1,0,0,0,0],
    ... [0,0,0,0,1,1,1,0,0,0],
    ... [0,0,0,0,0,1,1,1,0,0],
    ... [0,0,0,0,0,0,1,1,1,0],
    ... [0,0,0,0,0,0,0,1,1,1],
    ... [0,0,0,0,0,0,0,0,1,1],
    ... [0,0,0,0,0,0,0,0,0,1]
    ... ]
    >>> is_transitive(M_big)
    False

    >>> M_big_not = [
    ... [1,1,0,0,0,0,0,0,0,0],
    ... [0,1,1,0,0,0,0,0,0,0],
    ... [0,0,1,1,0,0,0,0,0,0],
    ... [0,0,0,1,0,0,0,0,0,0],
    ... [0,0,0,0,1,1,0,0,0,0],
    ... [0,0,0,0,0,1,0,1,0,0],
    ... [0,0,0,0,0,0,1,0,0,0],
    ... [0,0,0,0,0,0,0,1,1,0],
    ... [0,0,0,0,0,0,0,0,1,1],
    ... [0,0,0,0,0,0,0,0,0,1]
    ... ]
    >>> is_transitive(M_big_not)
    False
    '''
    for index, row in enumerate(matrix):
        for j_index, value in enumerate(row):
            if value == 1:
                for k in range(len(matrix)):
                    if matrix[j_index][k] == 1:
                        if matrix[index][k] != 1:
                            return False
    return True


#############################################################
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
