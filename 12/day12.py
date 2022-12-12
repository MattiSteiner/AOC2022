from networkx import grid_2d_graph
from networkx import dijkstra_path_length


with open("day12.txt") as f:
    grid = [list(x.strip()) for x in f]


S_pos = (-1,-1)
E_pos = (-1,-1)
pos_s = list()

for rowN, row in enumerate(grid):
    for colN, col in enumerate(row):
        if col == "S":
            S_pos = (rowN,colN)
            grid[rowN][colN] = "a"

        if col == "E":
            E_pos = (rowN,colN)
            grid[rowN][colN] = "z"

        if col == "a":
            pos_s.append((rowN,colN))

g = grid_2d_graph(len(grid), len(grid[0]))
grid = [[ord(col)-97 for col in row] for row in grid]

def weight(x,y,edge_d):
    if grid[x[0]][x[1]] < grid[y[0]][y[1]] -1:
        return None
    return 1

print("Part 1 len: ",dijkstra_path_length(g,S_pos,E_pos,weight))


min_len = 10000
min_pos = (-1,-1)

for a_pos in pos_s:
    try: 
        walk_dist = dijkstra_path_length(g,a_pos,E_pos,weight)
    except:
        pass
    if walk_dist < min_len:
        min_len = walk_dist
        min_pos = a_pos

print("Part 2 len:", min_len, min_pos)



