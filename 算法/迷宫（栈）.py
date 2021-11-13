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


def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1, y1))  # 起点
    while (len(stack)>0):
        curnode = stack[-1] # 当前节点 (取栈顶)
        if curnode[0] == x2 and curnode[1] == y2:
            # 走到终点了
            for p in stack:
                print(p)
            return True
        # x，y四个方向移动 上：x-1,y 下：x+1,y 左：x,y-1 右：x,y+1
        for dir in dirs:
            nextnode = dir(curnode[0], curnode[1]) # 上下左右移动的下个节点
            # 如果下个节点能走
            if maze[nextnode[0]][nextnode[1]] == 0:
                stack.append(nextnode)
                maze[nextnode[0]][nextnode[1]] = 2 # 标记为已经走过
                break
        else:
            maze[nextnode[0]][nextnode[1]] = 2
            stack.pop()

    else:
        print("没有路走")
        return False


maze_path(1,1,8,8)


