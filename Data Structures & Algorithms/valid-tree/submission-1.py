class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = defaultdict(list)

        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)

        seen = defaultdict(bool)
        dfs = deque([(0,-1)])
        seen[0] = True
        while dfs:
            node,parent = dfs.popleft()
            for edge in tree[node]:
                if edge == parent:
                    continue
                if seen[edge]:
                    return False
                seen[edge] = True
                dfs.append((edge,node))
        
        return seen.keys() == tree.keys()





        


        