from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            tmp = dist[:]  
            for u, v, price in flights:
                if dist[u] != INF and dist[u] + price < tmp[v]:
                    tmp[v] = dist[u] + price
            dist = tmp
        
        return -1 if dist[dst] == INF else dist[dst]
