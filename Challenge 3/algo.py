import random

DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
MOVES = ['d', 'u', 'r', 'l']

def bfs(gamedata):
    print(gamedata)
    visited = set()
    queue = [(tuple(gamedata['currentPosition']), [])]

    while queue:
        node, path = queue.pop(0)

        if node in visited:
            continue

        # if the node is a coin
        if is_coin(gamedata, node):
            return path

        for index, direction in enumerate(DIRECTIONS):
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            if not out_of_bound(neighbor) and not is_wall(gamedata, neighbor):
                queue.append((neighbor, path + [MOVES[index]]))

        visited.add(node)

    node = tuple(gamedata['currentPosition'])
    while True:
        
        # get random direction
        index = random.randrange(0, len(DIRECTIONS))
        direction = DIRECTIONS[index]
        neighbor = (node[0] + direction[0], node[1] + direction[1])

        if not out_of_bound(neighbor) and not is_wall(gamedata, neighbor):
            return [MOVES[index]]

def is_coin(gamedata, node) -> bool:
    """determines whether the node is a coin or not"""

    for coin_type in ['coin1', 'coin2', 'coin3']:
        for coin in gamedata[coin_type]:
            if node == tuple(coin):
                return True

    return False

def is_wall(gamedata, node) -> bool:
    """determines whether the node is a wall or not"""
    
    for wall in gamedata['walls']:
        if node == tuple(wall):
            return True

    return False

def out_of_bound(node) -> bool:    
    return node[0] < 0 or node[1] < 0 or node[0] >= 10 or node[1] >= 10