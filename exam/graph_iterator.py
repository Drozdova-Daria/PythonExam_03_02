import functools


def print_iter(graph_iter):
    @functools.wraps(graph_iter)
    def graph_iter_decorator(*args, **kwargs):
        inner_graph_iter = graph_iter(*args, **kwargs)
        file = open("result.txt", "w")
        for result in inner_graph_iter:
            file.write(result[0] + ": " + str(result[1]) + '\n')
            yield result
    return graph_iter_decorator


@print_iter
class GraphIterator:
    def __init__(self, graph):
        self.graph = graph

    def work(self):
        for key in self.graph:
            yield key, len(self.graph[key])

    def __iter__(self):
        return self.work()
