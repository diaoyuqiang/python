from collections import deque
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x, y-1)
]


def print_t(path):
    curnode = path[-1]
    real_path = []
    while curnode[2] != -1:
        real_path.append(curnode[0:2])
        curnode = path[curnode[2]]
    real_path.append(curnode[0:2]) # 把起点放进去
    real_path.reverse()
    for node in real_path:
        print(node)


def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curnode = queue.pop()
        path.append(curnode)
        if curnode[0] == x2 and curnode[1] == y2: # 终点
            print_t(path)
            return True

        for dir in dirs:
            nextnode = dir(curnode[0],curnode[1])
            if maze[nextnode[0]][nextnode[1]] ==0:
                queue.append((nextnode[0],nextnode[1],len(path) - 1)) # nextnode由现节点找到
                maze[nextnode[0]][nextnode[1]] = 2 # 标记已经走过
    else:
        print("没有路")
        return False

maze_path_queue(1,1,8,8)