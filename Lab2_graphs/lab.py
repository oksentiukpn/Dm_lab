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
        ver = arr.pop() # taking last elm from stack

        if ver not in visited: # proccesing this elm
            visited.append(ver)
            neighbors = graph.get(ver, [])
            for i in range(len(neighbors) - 1, -1, -1): # adding links to stack for future
                if neighbors[i] not in visited:
                    arr.append(neighbors[i])
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
        v = arr.pop(0) # FIFO-fum
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

#########################
# Task4
def adjacency_matrix_radius(graph: list[list[int]]) -> int:
    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]])
    1
    """
    graph_dict = {}

    for i in range(len(graph)):
        graph_dict[i] = []

    all_vertices = list(graph_dict.keys())

    for ind, row in enumerate(graph):
        for indx, element in enumerate(row):
            if element == 1:
                graph_dict[all_vertices[ind]].append(all_vertices[indx])


    def breadth_first_search(graph_dict: dict, vertex) -> dict:
        queue = [vertex]
        order = 0
        eccentricities = {vertex: 0}

        while order < len(queue):
            vertex = queue[order]
            order += 1

            for adjacent_vertex in graph_dict[vertex]:
                if adjacent_vertex not in eccentricities:
                    eccentricities[adjacent_vertex] = eccentricities[vertex] + 1
                    queue.append(adjacent_vertex)

        return eccentricities

    all_eccentricities = []
    for vertex in graph_dict:
        all_eccentricities.append(max((breadth_first_search(graph, vertex)).values()))

    radius = min(all_eccentricities)

    return radius



def adjacency_dict_radius(graph: dict[int, list[int]]) -> int:
    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]})
    1
    """
    def breadth_first_search(graph: dict, vertex) -> dict:
        queue = [vertex]
        order = 0
        eccentricities = {vertex: 0}

        while order < len(queue):
            vertex = queue[order]
            order += 1

            for adjacent_vertex in graph[vertex]:
                if adjacent_vertex not in eccentricities:
                    eccentricities[adjacent_vertex] = eccentricities[vertex] + 1
                    queue.append(adjacent_vertex)

        return eccentricities

    all_eccentricities = []
    for vertex in graph:
        all_eccentricities.append(max((breadth_first_search(graph, vertex)).values()))

    radius = min(all_eccentricities)

    return radius



#########################
# Task5

def find_all_cycles_adjacency_matrix(graph: list[list[int]]) -> list[list]:
    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :returns list[list]: list of cycles of the graph
    >>> adjacency_matrix = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
    >>> find_all_cycles_adjacency_matrix(adjacency_matrix)
    [[0, 1, 2, 0]]
    """
    graph_dict = {}

    for i in range(len(graph)):
        graph_dict[i] = []

    all_vertices = list(graph_dict.keys())

    for ind, row in enumerate(graph):
        for indx, element in enumerate(row):
            if element == 1:
                graph_dict[all_vertices[ind]].append(all_vertices[indx])


    all_cycles = []
    already_visited = set()
    def dfs(current_vertex, path, path_set, dfs_stack):
        """
        Depth-First Search для пошуку циклів.
        """
        path.append(current_vertex)
        path_set.add(current_vertex)
        dfs_stack.add(current_vertex)

        try:
            for adjacent_vertex in graph_dict[current_vertex]:

                if adjacent_vertex in path_set:
                    cycle_start_index = path.index(adjacent_vertex)
                    cycle = path[cycle_start_index:] + [adjacent_vertex]

                    if len(set(cycle[:-1])) >= 3:
                        all_cycles.append(cycle)

                elif adjacent_vertex not in already_visited and adjacent_vertex not in dfs_stack:
                    dfs(adjacent_vertex, path, path_set, dfs_stack)

            path.pop()
            path_set.remove(current_vertex)
            dfs_stack.remove(current_vertex)
        except KeyError:
            pass


    for start_vertex in graph_dict:
        if start_vertex not in already_visited:
            already_visited.add(start_vertex)
            dfs(start_vertex, [], set(), set())


    no_repeats_cycles = set([tuple(lst) for lst in all_cycles])
    no_repeats_cycles = [list(tuples) for tuples in list(no_repeats_cycles)]

    return no_repeats_cycles




def find_all_cycles_dict(graph: dict[int, list[int]]) -> list[list]:
    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :returns list[list]: list of cycles of the graph
    >>> graph = {1: [2], 2: [3], 3: [1, 4], 4: [2]}
    >>> find_all_cycles_dict(graph)
    [[1, 2, 3, 1], [2, 3, 4, 2]]
    """
    all_cycles = []
    already_visited = set()

    def dfs(current_vertex, path, path_set, dfs_stack):
        """
        Depth-First Search для пошуку циклів.
        """
        path.append(current_vertex)
        path_set.add(current_vertex)
        dfs_stack.add(current_vertex)

        try:
            for adjacent_vertex in graph[current_vertex]:

                if adjacent_vertex in path_set:
                    cycle_start_index = path.index(adjacent_vertex)
                    cycle = path[cycle_start_index:] + [adjacent_vertex]

                    if len(set(cycle[:-1])) >= 3:
                        all_cycles.append(cycle)

                elif adjacent_vertex not in already_visited and adjacent_vertex not in dfs_stack:
                    dfs(adjacent_vertex, path, path_set, dfs_stack)

            path.pop()
            path_set.remove(current_vertex)
            dfs_stack.remove(current_vertex)
        except KeyError:
            pass


    for start_vertex in graph:
        if start_vertex not in already_visited:
            already_visited.add(start_vertex)
            dfs(start_vertex, [], set(), set())


    no_repeats_cycles = set([tuple(lst) for lst in all_cycles])
    no_repeats_cycles = [list(tuples) for tuples in list(no_repeats_cycles)]

    no_repeats_cycles = sorted(no_repeats_cycles)

    return no_repeats_cycles

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
