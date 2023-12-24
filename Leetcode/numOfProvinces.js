const dfs = (i, isConnected, visitedCities) => {
    for (let j = 0; j < isConnected.length; j++){
        if (isConnected[i][j] == 1 && !visitedCities.has(j)){
            visitedCities.add(j);
            dfs(j, isConnected, visitedCities);
        }
    }
}



const findCircleNum = (isConnected) => {
    let visitedCities = new Set();
    let totalProvinces = 0;
    
    // start from these cities (row wise tarversal in nxn array)
    for (let i = 0; i < isConnected.length; i++){
        // haven't visited this city yet
        if (!visitedCities.has(i)){
            dfs(i, isConnected, visitedCities);
            totalProvinces += 1;
        }
    }
    return totalProvinces;
}

// driver function
const isConnected = [[1,1,0],[1,1,0],[0,0,1]];
console.log(findCircleNum(isConnected))