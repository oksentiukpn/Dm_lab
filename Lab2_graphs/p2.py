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
