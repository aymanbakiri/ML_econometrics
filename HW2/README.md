# MGT-424 — Homework 2

### Question 1 — Bayesian Networks and Chow–Liu Trees

We approximate the joint distribution of four binary variables \(X_1, X_2, X_3, X_4\) using a tree-structured Bayesian network. The Chow–Liu tree is built as a **maximum-weight spanning tree** on pairwise mutual informations.

**File(s)**

| Path | Description |
|------|-------------|
| `question1/q1_chow_liu.py` | Kruskal’s algorithm from scratch + `networkx` verification |

**Run Question 1**

```bash
python3 question1/q1_chow_liu.py
```

**Result (maximum-weight spanning tree)**

- Edges: `X1–X2` (0.82), `X3–X4` (0.75), `X2–X3` (0.51)
- Total weight: **2.08**

Requires `networkx` for the verification section only (Part v.ii).
