import math
from sys import stdin,stdout
import bisect
from collections import Counter
import numpy as np
def BFS_FOR_UNDIRECTED_GRAPH_USING_ADJACENCY_LIST(graph):
    visited = [False] * len(graph)
    queue = []
    queue.append(0)
    BFS = []
    while (len(queue) != 0):
        v = queue[0]
        del queue[0]
        if (visited[v] == False):
            BFS.append(v)
        if (visited[v] == False):
            visited[v] = True
            for i in range(0, len(graph[v])):
                queue.append(graph[v][i])
    return BFS
cop=[Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 7: 1, 8: 1, 10: 1, 11: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 20: 1, 22: 1, 23: 1, 25: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 35: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1, 11: 1, 12: 1, 13: 1, 14: 1, 16: 1, 17: 1, 18: 1, 19: 1, 21: 1, 22: 1, 23: 1, 24: 1, 26: 1, 27: 1, 28: 1, 29: 1, 31: 1, 32: 1, 33: 1, 34: 1, 36: 1, 37: 1, 38: 1, 39: 1, 41: 1, 42: 1, 43: 1, 44: 1, 46: 1, 47: 1, 48: 1, 49: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 7: 1, 8: 1, 10: 1, 11: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 20: 1, 22: 1, 23: 1, 25: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 35: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1, 50: 1}), Counter({3: 1, 7: 1, 9: 1, 11: 1, 13: 1, 17: 1, 19: 1, 21: 1, 23: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1}), Counter({2: 1, 4: 1, 7: 1, 8: 1, 11: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 22: 1, 23: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 37: 1, 38: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({3: 1, 7: 1, 9: 1, 11: 1, 13: 1, 17: 1, 19: 1, 21: 1, 23: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 8: 1, 10: 1, 11: 1, 13: 1, 16: 1, 17: 1, 19: 1, 20: 1, 22: 1, 23: 1, 25: 1, 26: 1, 29: 1, 31: 1, 32: 1, 34: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1, 11: 1, 12: 1, 13: 1, 14: 1, 16: 1, 17: 1, 18: 1, 19: 1, 21: 1, 22: 1, 23: 1, 24: 1, 26: 1, 27: 1, 28: 1, 29: 1, 31: 1, 32: 1, 33: 1, 34: 1, 36: 1, 37: 1, 38: 1, 39: 1, 41: 1, 42: 1, 43: 1, 44: 1, 46: 1, 47: 1, 48: 1, 49: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 7: 1, 8: 1, 10: 1, 11: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 20: 1, 22: 1, 23: 1, 25: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 35: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 7: 1, 8: 1, 10: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 20: 1, 23: 1, 25: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 35: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 46: 1, 47: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 6: 1, 8: 1, 9: 1, 11: 1, 12: 1, 13: 1, 16: 1, 17: 1, 18: 1, 19: 1, 22: 1, 23: 1, 24: 1, 26: 1, 27: 1, 29: 1, 31: 1, 32: 1, 33: 1, 34: 1, 36: 1, 37: 1, 38: 1, 39: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 48: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 5: 1, 7: 1, 8: 1, 10: 1, 11: 1, 14: 1, 16: 1, 17: 1, 19: 1, 20: 1, 22: 1, 23: 1, 25: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 35: 1, 37: 1, 38: 1, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1, 50: 1}), Counter({3: 1, 7: 1, 9: 1, 11: 1, 13: 1, 17: 1, 19: 1, 21: 1, 23: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({5: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 37: 1, 41: 1, 43: 1, 47: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 23: 1, 25: 1, 27: 1, 29: 1, 31: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 4: 1, 7: 1, 8: 1, 11: 1, 13: 1, 14: 1, 16: 1, 17: 1, 19: 1, 22: 1, 23: 1, 26: 1, 28: 1, 29: 1, 31: 1, 32: 1, 34: 1, 37: 1, 38: 1, 41: 1, 43: 1, 44: 1, 46: 1, 47: 1, 49: 1}), Counter({3: 1, 5: 1, 7: 1, 9: 1, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 1, 25: 1, 27: 1, 29: 1, 31: 1, 33: 1, 35: 1, 37: 1, 39: 1, 41: 1, 43: 1, 45: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 48: 1, 49: 1, 50: 1}), Counter({5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 25: 1, 29: 1, 31: 1, 35: 1, 37: 1, 41: 1, 43: 1, 47: 1, 49: 1}), Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 50: 1}), Counter({3: 1, 7: 1, 9: 1, 11: 1, 13: 1, 17: 1, 19: 1, 21: 1, 23: 1, 27: 1, 29: 1, 31: 1, 33: 1, 37: 1, 39: 1, 41: 1, 43: 1, 47: 1, 49: 1})]
prime=[47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
t=int(stdin.readline())
while(t>0):
    n=int(stdin.readline())
    A=[int(i) for i in stdin.readline().split()]
    co = []
    min = 0
    B = []
    d = Counter(A)
    values = np.array(A)
    C=[A[i] for i in range(0,n)]
    C.sort()
    #graph=[[]for y in range(0,n)]
    graph=[]
    '''
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if(math.gcd(A[i],A[j])==1):
                graph[i].append(j)
                graph[j].append(i)
    '''
    for i in range(0,len(A)):
        d1=cop[A[i]-2]
        d3=d1&d
        ii=[]
        for key in d3:
            searchval = key
            ii = np.where(values == searchval)[0]
            print(ii)
            graph.append(ii)
            '''
            for j in range(0,len(ii)):
                graph[i].append(ii[j])
            '''
    #print(graph)
    BFS=BFS_FOR_UNDIRECTED_GRAPH_USING_ADJACENCY_LIST(graph)
    if(len(BFS)==n):
        min=0
        B=A
    else:
        i = 0
        while (True):
            pos = bisect.bisect_right(C, prime[i])
            if (C[pos - 1] == prime[i] and pos - 1 > 0 and pos - 1 < n):
                i += 1
            else:
                if (i >= 0 and i < len(prime)):
                    A[n - 1] = prime[i]
                min = 1
                B = A
                break
    stdout.write(str(min)+'\n')
    for i in range(0,len(B)):
        stdout.write(str(B[i])+' ')
    stdout.write('\n')
    t -= 1