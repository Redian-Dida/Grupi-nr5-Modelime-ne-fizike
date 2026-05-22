import numpy as np

def calculate_pagerank(adj, damping=0.85, iterations=100, tol=1e-6):
    """
    Calculate PageRank scores for nodes in a graph.
    """
    n = adj.shape[0]
    out_links = adj.sum(axis=1)
    out_links[out_links == 0] = 1
    M = adj / out_links[:, np.newaxis]
    M = damping * M + (1 - damping) / n
    pr = np.ones(n) / n

    for _ in range(iterations):
        pr_new = M.T @ pr
        if np.linalg.norm(pr_new - pr) < tol:
            break
        pr = pr_new

    pr = pr / pr.sum()
    return pr

def get_spam_score(adj):
    """
    Calculate spam scores based on in-degree and out-degree.
    """
    n = adj.shape[0]
    in_degree = adj.sum(axis=0)
    out_degree = adj.sum(axis=1)
    max_degree = max(in_degree.max(), out_degree.max())
    if max_degree == 0:
        return np.zeros(n)

    spam = np.zeros(n)
    for i in range(n):
        if in_degree[i] == 0 and out_degree[i] > 0:
            spam[i] = min(1.0, out_degree[i] / max_degree)
        elif in_degree[i] > 0:
            spam[i] = max(0, (out_degree[i] - in_degree[i]) / max_degree)

    return spam / (spam.max() + 1e-10)

def calculate_hybrid_score(pagerank, spam_score, weight=0.1):
    """
    Calculate hybrid score combining PageRank with spam penalty.
    """
    hybrid = pagerank * (1 - weight * spam_score)
    hybrid = hybrid / hybrid.sum()
    return hybrid
