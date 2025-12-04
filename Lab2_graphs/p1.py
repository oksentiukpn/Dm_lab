'''
Lab2 Graphs
Tasks 1 2 3
'''
#############################################################
# Task 1

def read_file(filename: str):
    '''
    Docstring for read_file

    :param filename: Description
    :type filename: str
    #>>> read_file('input.dot')
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip().replace(';', '') for line in file.readlines()[1:-1]]
        lines = [line.split(' -> ') for line in lines]
    # return [(int(a), int(b)) for a, b in lines]
    return lines

def read_incidence_matrix(filename: str) -> list[list[int]]:
    """
    :param str filename: path to file
    :returns list[list[int]]: the incidence matrix of a given graph

    >>> read_incidence_matrix('input.dot')
    """
    vertices = set()
    lines = read_file(filename)
    for a, b in lines:
        vertices.add(a)
        vertices.add(b)
    n = len(vertices)
    matrix = [[0]*len(lines) for _ in range(n)]
    v_dict = {v: i for i, v in enumerate(sorted(vertices))}
    for i, (a, b) in enumerate(lines):
        a, b = v_dict[a], v_dict[b]
        if a != b:
            matrix[a][i] = -1
            matrix[b][i] = 1
        else:
            matrix[a][i] = 2
    return matrix



def read_adjacency_matrix(filename: str) -> list[list[int]]:
    """
    :param str filename: path to file
    :returns list[list[int]]: the adjacency matrix of a given graph

    #>>> read_adjacency_matrix('input.dot')
    """
    vertices = set()
    lines = read_file(filename)
    for a, b in lines:
        vertices.add(a)
        vertices.add(b)
    n = len(vertices)
    matrix = [[0]*n for _ in range(n)]
    v_dict = {v: i for i, v in enumerate(sorted(vertices))}
    for a, b in lines:
        a, b = v_dict[a], v_dict[b]
        matrix[a][b] += 1
    return matrix

def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict[int, list[int]]: the adjacency dict of a given graph

    #>>> read_adjacency_dict('input.dot')
    """
    lines = read_file(filename)
    result = {}

    for a, b in lines:
        result.setdefault(a, [])
        result.setdefault(b, [])
        result[a].append(b)

    return result
#############################################################


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
