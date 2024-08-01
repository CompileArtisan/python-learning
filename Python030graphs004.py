# implementation of weighted directed graphs using adjacency matrix
def main():
    ...
    
class Graph:
    def __init__(self, n):
        self.graph = [[0]*n for _ in range(n)]
        self.n = n
        
    def __str__(self):
        return f"{self.graph}"
    
    def add_edge(self, u, v, weight):
        try:
            self.graph[u,v] = weight
        except: 
            print("Error: Nodes Incorrect")
            
    def remove_edge(self, u, v):
        try:
            self.graph[u,v] = 0
        except: 
            print("Error: Nodes Incorrect")
            
    def has_self_loop(self):
        for i in range(self.n):
            if self.graph(i,i)>0:
                return True
        return False
    
    def has_parallel_edge(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] > 1:
                    return True
        return False
    
    
if __name__ == "__main__":
    main()