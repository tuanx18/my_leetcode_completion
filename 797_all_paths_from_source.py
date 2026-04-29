# [MEDIUM] https://leetcode.com/problems/all-paths-from-source-to-target/
# Completed 2026/04/29
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []

        def dfs(node, path):
            if node == target:
                res.append(path[:])
                return
            
            for next_node in graph[node]:
                dfs(next_node, path + [next_node])
        
        dfs(0, [0])
        return res