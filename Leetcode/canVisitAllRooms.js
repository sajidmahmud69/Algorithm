const dfs = (key, rooms, visitedRooms) => {
    if (visitedRooms.has(key)) return
    visitedRooms.add(key)
    rooms[key].forEach(k => {
        dfs(k, rooms. visitedRooms)
    });
}


const canVisitAllRooms = (rooms) => {
    let visitedRooms = new Set()
    dfs(0, rooms, visitedRooms)

    return visitedRooms.size === rooms.length
}


// driver function

const rooms = [[1],[2],[3],[]]
console.log(canVisitAllRooms(rooms))

const rooms2 = [[[1,3],[3,0,1],[2],[0]]]
console.log(canVisitAllRooms(rooms2))
