def main():
    graph = { "a" : ["c"],
              "b" : ["c", "e"],
              "c" : ["a", "b", "d", "e"],
              "d" : ["c"],
              "e" : ["c", "b"],
              "f" : []
            }

    print(generate_edges(graph))


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

if __name__ == '__main__':
    main()
