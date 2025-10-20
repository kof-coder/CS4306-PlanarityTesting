class HalfEdge:
    __slots__ = ("u","v","mate","next","prev")
    def __init__(self,u,v): self.u,self.v,self.mate,self.next,self.prev = u,v,None,None,None

class Embedding:
    # TODO: maintain circular order of incident edges per vertex
    # TODO: merge constraints during DFS backtracking
    pass

