"""
Question 1: Chow-Liu Tree for four binary variables X1, X2, X3, X4.

Part (v.i): Build the maximum-weight spanning tree from scratch using
Kruskal's algorithm with a union-find data structure (path compression
and union by rank).

Part (v.ii): Verify the result using networkx.
"""

variables = ["X1", "X2", "X3", "X4"]

edges = [
    ("X1", "X2", 0.82),
    ("X1", "X3", 0.10),
    ("X1", "X4", 0.41),
    ("X2", "X3", 0.51),
    ("X2", "X4", 0.33),
    ("X3", "X4", 0.75),
]


def find(parent, x):
    """Find the representative of x's component, with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    """Union the components of x and y by rank.

    Returns True if x and y were in different components (the union
    actually happened), False if they were already in the same
    component (which means adding the edge would create a cycle).
    """
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return True


def chow_liu_tree_from_scratch(variables, edges):
    """Build the maximum-weight spanning tree using Kruskal's algorithm.

    Edges with higher mutual information are added first. An edge is
    only kept if it does not form a cycle. We stop once the tree has
    len(variables) - 1 edges.
    """
    sorted_edges = sorted(edges, key=lambda e: e[2], reverse=True)

    parent = {v: v for v in variables}
    rank = {v: 0 for v in variables}

    tree_edges = []
    total_weight = 0.0

    for u, v, w in sorted_edges:
        if union(parent, rank, u, v):
            tree_edges.append((u, v, w))
            total_weight += w
            if len(tree_edges) == len(variables) - 1:
                break

    return tree_edges, total_weight


if __name__ == "__main__":
    print("=" * 60)
    print("Part (v.i): Chow-Liu tree from scratch (Kruskal)")
    print("=" * 60)

    tree_edges, total_weight = chow_liu_tree_from_scratch(variables, edges)

    print("Selected edges of the maximum-weight spanning tree:")
    for u, v, w in tree_edges:
        print(f"  {u} -- {v}   (I = {w})")
    print(f"Total weight: {total_weight:.2f}")

    print()
    print("=" * 60)
    print("Part (v.ii): Verification using networkx")
    print("=" * 60)

    import networkx as nx

    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    nx_tree = nx.maximum_spanning_tree(G, weight="weight")

    nx_tree_edges = [(u, v, d["weight"]) for u, v, d in nx_tree.edges(data=True)]
    nx_total_weight = sum(w for _, _, w in nx_tree_edges)

    print("Networkx maximum spanning tree edges:")
    for u, v, w in nx_tree_edges:
        print(f"  {u} -- {v}   (I = {w})")
    print(f"Total weight: {nx_total_weight:.2f}")

    scratch_edge_set = {frozenset((u, v)) for u, v, _ in tree_edges}
    nx_edge_set = {frozenset((u, v)) for u, v, _ in nx_tree_edges}

    print()
    if scratch_edge_set == nx_edge_set:
        print("Both implementations return the SAME set of undirected edges.")
    else:
        print("The two implementations return DIFFERENT sets of edges.")
        print(f"  From scratch: {scratch_edge_set}")
        print(f"  Networkx:     {nx_edge_set}")
