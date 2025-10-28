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
    with open('result.csv', 'w', encoding='utf-8') as file:
        matrix = ["".join([str(j) for j in i]) for i in matrix] # convert matrix to list of rows
        file.write("\n".join(matrix)) # write list converted to fully str
    return True
##############################################################
# 2
def reflexive_closure(matrix: list) -> list:
    '''
    This function returns the reflexive closure of a binary relation

    :param matrix: list[list[int]], square binary matrix representing the relation
    :return: list[list[int]] | None, matrix of the reflexive closure or None if invalid input
    '''
    n = len(matrix)
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def symmetric_closure(matrix: list) -> list:
    '''
    This function returns the symmetric closure of a binary relation

    :param matrix: list[list[int]], square binary matrix representing the relation
    :return: list[list[int]] | None, matrix of the symmetric closure or None if invalid input
    '''
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    return matrix
##############################################################
# 3
def warshall(matrix: list) -> list:
    '''
    This function returns the transitive closure of a binary relation
    using Warshall's algorithm.

    :param matrix: list[list[int]], square binary matrix representing the relation
    :return: list[list[int]], matrix of the transitive closure or None if invalid input
    >>> warshall([[0, 1], [0, 0]])
    [[0, 1], [0, 0]]

    >>> warshall([[0, 1, 0],
    ...           [0, 0, 1],
    ...           [0, 0, 0]])
    [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    '''
    w = matrix[:]
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            if i != k and w[i][k] == 1:
                for j in range(n):
                    w[i][j] = w[i][j] or w[k][j]
    return w
##############################################################
# 4
def relation_breakdown(relation: list | set[tuple], is_matrix: bool) -> list:
    '''
    Break down a equivalent relation into equivalence classes.

    if matrix given:
    The input matrix represents a relation `R` on a finite set of elements
    {0, 1, ..., n-1}, where `matrix[i][j] == 1` means "element i is related to element j".

    This function finds all equivalence classes — groups of elements that are
    mutually related (directly or through a chain of relations).

    :param relation: list | set, our equivalent matrix or relation
    :return: list, equivalent classes
    >>> relation_breakdown([[1, 1, 0], [1, 1, 0], [0, 0, 1]], True)
    [[0, 1], [2]]
    >>> relation_breakdown([[1, 0, 0], [0, 1, 0], [0, 0, 1]], True)
    [[0], [1], [2]]
    >>> relation_breakdown([[1, 1, 1],
    ...                     [1, 1, 1],
    ...                     [1, 1, 1]], True)
    [[0, 1, 2]]
    >>> relation_breakdown([[1, 0, 0, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 0, 0, 1]], True)
    [[0], [1, 2], [3]]
    >>> relation_breakdown([[1, 1, 0, 0],
    ...                     [1, 1, 1, 0],
    ...                     [0, 1, 1, 0],
    ...                     [0, 0, 0, 1]], True)
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
    >>> relation_breakdown(big_matrix, True)
    [[0, 1], [2, 3, 4], [5, 6], [7, 8, 9]]
    >>> relation = {(1,1)}
    >>> relation_breakdown(relation, False)
    [{1}]
    >>> relation = {(1,1), (1,2), (2,1), (2,2)}
    >>> relation_breakdown(relation, False)
    [{1, 2}]
    >>> relation = {(1,2), (2,1), (3,4), (4,3), (1,1), (2,2), (3,3), (4,4)}
    >>> relation_breakdown(relation, False)
    [{1, 2}, {3, 4}]
    >>> relation = {(1,1), (2,2), (3,3), (4,4)}
    >>> relation_breakdown(relation, False)
    [{1}, {2}, {3}, {4}]

    >>> relation = {(1,2), (2,1), (2,2), (1,1), (3,3)}
    >>> relation_breakdown(relation, False)
    [{1, 2}, {3}]

    >>> relation = {(1,2), (2,1), (3,4), (4,3), (5,5), (1,1), (2,2), (3,3), (4,4)}
    >>> relation_breakdown(relation, False)
    [{1, 2}, {3, 4}, {5}]
    '''
    if is_matrix: # if given matrix
        matrix = relation
        classes = []
        def add_to_classes(index: int, j_index: int):
            '''Function for adding elements to classes and checking place for them'''
            if not classes: # if list is empty
                classes.append([index])
            for i, m in enumerate(classes): # check for existance in classes
                if index in m and j_index in m: # if both of them already in classes just skip
                    continue
                elif index in m and j_index not in m: # if only index in
                    classes[i].append(j_index)
                    break
                elif index not in m and j_index in m: # if only j_index in
                    classes[i].append(index)
                    break
                else: # if none of them in
                    if i + 1 == len(classes): # if only we went through every element and stil None
                        if index != j_index:
                            classes.append([j_index, index])
                        else:
                            classes.append([index])
                        break
                    continue

        for index, row in enumerate(matrix):
            for j_index, element in enumerate(row):
                if element == 1:
                    add_to_classes(index, j_index) # Adding to classes if not already in
        return classes
    else:
        elements = {j for i in relation for j in i} # all elements
        dictionary = {e: {e} for e in elements} # every element in class
        for a, b in relation: # merging together if they in relation
            together = dictionary[a] | dictionary[b]
            for i in together:
                dictionary[i] = together
        classes = [dictionary[i] for i in elements]
        result = []
        # removing duplicates
        for i in classes:
            if i not in result:
                result.append(i)
        return result

#############################################################
# 5
def is_transitive(relation: list | set[tuple], is_matrix: bool) -> bool:
    '''
    Checks if relation is transitive

    A relation R is transitive if for all i, j, k:
    (i,j) ∈ R and (j,k) ∈ R ⇒ (i,k) ∈ R

    :param relation: list | set[tuple], relation or matrix
    :return: bool, True or False
    >>> M = [
    ...     [1, 1, 0],
    ...     [0, 1, 1],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M, True)
    False

    >>> M2 = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M2, True)
    True

    >>> M3 = [
    ...     [1, 0, 0],
    ...     [0, 1, 0],
    ...     [0, 0, 1]
    ... ]
    >>> is_transitive(M3, True)
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
    >>> is_transitive(M_big, True)
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
    >>> is_transitive(M_big_not, True)
    False
    >>> is_transitive({(0, 1), (1, 2), (0, 2)}, False)
    True
    >>> is_transitive({(0, 1), (1, 2)}, False)
    False
    >>> is_transitive({(0, 1), (1, 2), (0, 2), (2, 5), (0, 5), (1, 5)}, False)
    True
    >>> is_transitive({(3, 4), (4, 5)}, False)
    False
    '''
    if is_matrix: # for matrix
        matrix = relation
        for index, row in enumerate(matrix):
            for j_index, value in enumerate(row):
                if value == 1:
                    for k in range(len(matrix)):
                        if matrix[j_index][k] == 1:
                            if matrix[index][k] != 1:
                                return False
    else: # for relation
        for a, b in relation:
            for c, d in relation:
                if b == c:
                    if (a, d) not in relation:
                        return False
    return True
#############################################################
# 6
def count_transitive(n: int) -> int:
    '''
    This function counts number of transitive relations
    on set of n elements
    !!! If n > 4 program will think very long time because of big amount of relations
    :param n: int, number of elemets in set
    :return: int, number of tranitive relations
    >>> count_transitive(1)
    2
    >>> count_transitive(2)
    13
    >>> count_transitive(3)
    171
    >>> count_transitive(4)
    3994
    '''

    total = 0
    for num in range(pow(2, n*n)):
        matrix = [[0]*n for _ in range(n)]
        k = num
        for i in range(n):
            for j in range(n):
                matrix[i][j] = k % 2
                k //= 2
        if is_transitive(matrix, True):
            total += 1
    return total


#############################################################
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())


#############################################################
