class Solution(object):
    def findRedundantConnection(self, edges):
        parent={}

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            parentX=find(x)
            parentY=find(y)

            if parentX==parentY: return True

            parent[parentY]=parentX
            return False
        
        for u,v in edges:
            if u not in parent:
                parent[u]=u
            if v not in parent:
                parent[v]=v
            
            if union(u,v):
                return [u,v]
