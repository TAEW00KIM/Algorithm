import sys
input = sys.stdin.readline

class Tree():
    def __init__(self, arr):
        self.n = len(arr)
        self.maxtree = [0] * (4 * self.n)
        self.mintree = [0] * (4 * self.n)
        
        self.buildmax(arr, 0, self.n - 1, 1)
        self.buildmin(arr, 0, self.n - 1, 1)
        
    def buildmin(self, arr, left, right, node):
        if left == right:
            self.mintree[node] = arr[left]
            return

        mid = (left + right) // 2
        self.buildmin(arr, left, mid, node * 2)
        self.buildmin(arr, mid + 1, right, node * 2 + 1)
        self.mintree[node] = min(self.mintree[node * 2], self.mintree[node * 2 + 1])
    
    def buildmax(self, arr, left, right, node):
        if left == right:
            self.maxtree[node] = arr[left]
            return
        
        mid = (left + right) // 2
        self.buildmax(arr, left, mid, node * 2)
        self.buildmax(arr, mid + 1, right, node * 2 + 1)
        self.maxtree[node] = max(self.maxtree[node * 2], self.maxtree[node * 2 + 1])
        
    def query_min(self, left, right, node, node_left, node_right):
        if node_right < left or right < node_left: return float('inf')
        if left <= node_left and node_right <= right: return self.mintree[node]
        
        node_mid = (node_left + node_right) // 2
        
        return min(self.query_min(left, right, node * 2, node_left, node_mid),
                   self.query_min(left, right, node * 2 + 1, node_mid + 1, node_right))
        
    def query_max(self, left, right, node, node_left, node_right):
        if node_right < left or right < node_left: return 0
        if left <= node_left and node_right <= right: return self.maxtree[node]
        
        node_mid = (node_left + node_right) // 2
        
        return max(self.query_max(left, right, node * 2, node_left, node_mid), 
                   self.query_max(left, right, node * 2 + 1, node_mid + 1, node_right))
    
    def get_min(self, left, right):
        return self.query_min(left, right, 1, 0, self.n - 1)
        
    def get_max(self, left, right):
        return self.query_max(left, right, 1, 0, self.n - 1)
    
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
pair = [map(int, input().split()) for _ in range(m)]

tree = Tree(arr)
for a, b in pair:
    print(tree.get_min(a - 1, b - 1), tree.get_max(a - 1, b - 1))
