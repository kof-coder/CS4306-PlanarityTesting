PLANARITY-HT(G):
  run DFS from each unvisited vertex:
    record order[u], low[u], parent[u]
    push traversed edges on stack
    if low[v] >= order[u]:  # u - v is a DFS-tree edge
        B ← pop edges until (u,v) popped
        if not EMBED-BLOCK(B): return NON-PLANAR
  return PLANAR

EMBED-BLOCK(B):
  init embedding E for block B
  for edges/paths discovered in DFS order:
      if ADD-TO-EMBEDDING(E, item) violates constraints:
          return False
  return True



THIS IS A CONCISE DRAFT
