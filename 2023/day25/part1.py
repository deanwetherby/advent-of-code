import logging
import pathlib
import sys

import networkx as nx


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()


def read_data(input: pathlib.Path) -> list[str]:
    return input.read_text().splitlines()


def build_graph(data: list[str]) -> nx.Graph:
    graph = nx.Graph()
    for line in data:
        node, connections = line.split(":")
        for connection in connections.strip().split(" "):
            graph.add_edge(node.strip(), connection.strip())
    return graph


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=pathlib.Path, default="example.txt")
    args = parser.parse_args()
    logger.info(args)
    data = read_data(args.input)
    graph = build_graph(data)
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    a, b = nx.connected_components(graph)
    logger.info(f"answer={len(a) * len(b)}")
