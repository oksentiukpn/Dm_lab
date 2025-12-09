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

    #>>> read_incidence_matrix('input.dot')
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

def read_adjacency_dict(filename: str) -> dict[any, list[int]]:
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
# Task 2

def recursive_adjacency_dict_dfs(graph: dict, start: int, visited: list = None) -> list[int]:
    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    # if point is not in visited
    if start not in visited:
        visited.append(start)
        # finding all links
        links = graph.get(start, [])

        for link in links: # repeat for all links
            recursive_adjacency_dict_dfs(graph, link, visited)
    return visited

def recursive_adjacency_matrix_dfs(graph: list, start: int, visited: list = None) -> list[int]:
    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)

    for index, value in enumerate(graph[start]):
        if value: # if value >= 1 than its true and at least 1 link connected
            if index not in visited:
                recursive_adjacency_matrix_dfs(graph, index, visited)

    return visited
#############################################################
# Task 3
def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    visited = []
    arr = [start]
    while arr:
        ver = arr.pop(0) # taking first elm from stack

        if ver not in visited: # proccesing this elm
            visited.append(ver)

            links = graph.get(ver, [])

            for link in links: # adding links from this elm to stack for future processing
                if link not in visited:
                    arr.append(link)
    return visited


def iterative_adjacency_matrix_dfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    visited = []
    arr = [start]
    while arr:
        v = arr.pop() #taking last elm from arr, Last In first out
        if v not in visited:
            visited.append(v)
            row = graph[v]
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 1 and i not in visited:
                    arr.append(i)

    return visited



def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    visited = []
    arr = [start]
    while arr:
        v = arr.pop(0) # FIFO
        if v not in visited:
            visited.append(v)

        for e in graph.get(v, []):
            if e not in visited:
                visited.append(e)
                arr.append(e)

    return visited



def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    visited = []
    arr = [start]
    while arr:
        v = arr.pop(0) # FIFO
        if v not in visited:
            visited.append(v)
        for i, e in enumerate(graph[v]):
            if e == 1 and i not in visited:
                visited.append(i)
                arr.append(i)
    return visited

#############################################################

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
