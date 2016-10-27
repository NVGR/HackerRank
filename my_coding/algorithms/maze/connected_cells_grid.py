"""def get_biggest_region(grid):
    adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
"""


def get_biggest_region(n, m, grid):
    visited = [[False for _ in xrange(m)] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(m):
            if not visited[i][j] and grid[i][j] == 1:
                global cur_area
                cur_area = 0
                dfs(visited, grid, i, j, n, m)
                return max_val


def dfs(visited, mat, i, j, n, m):
    visited[i][j] = True
    global cur_area
    cur_area += 1
    global max_val
    max_val = max(max_val, cur_area)

    # adjacency = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
    # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for adj in adjacency:
        adj_i = i + adj[0]
        adj_j = j + adj[1]
        if 0 <= adj_i < n and 0 <= adj_j < m and not visited[adj_i][adj_j] and mat[adj_i][adj_j] == 1:
            dfs(visited, mat, adj_i, adj_j, n, m)


if __name__ == '__main__':
    cur_area = 0
    max_val = -1

    n = int(raw_input().strip())
    m = int(raw_input().strip())

    # Adjacency elements
    adjacency = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
    # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    grid = []
    for grid_i in xrange(n):
        grid_temp = map(int, raw_input().strip().split(' '))
        # grid_temp = [int(x) for x in raw_input().strip().split(' ')]
        grid.append(grid_temp)

    print get_biggest_region(n, m, grid)



