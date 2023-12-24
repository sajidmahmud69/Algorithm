def canVisitAllRooms(rooms):
    def dfs(room):
        if room in visited:
            return

        visited.add(room)
        for key in rooms[room]:
            dfs(key)

    visited = set()
    dfs(0)

    return len(visited) == len(rooms)


if __name__ == '__main__':
    rooms = [[1],[2],[3],[]]
    print(canVisitAllRooms(rooms))

    rooms = [[1,3],[3,0,1],[2],[0]]
    print(canVisitAllRooms(rooms))
