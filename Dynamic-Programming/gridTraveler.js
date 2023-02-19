// You have a m rows and n cols grid
// You can only move right or down
// Your goal is to find out how many ways you can travel the grid

// No memoization grid traveler

const gridTraveler = (m, n) => {
	// base case
	if (m === 1 && n === 1) return 1;   // 1x1 grid
	if (m === 0 || n === 0) return 0;	// 0x0 grid or false dimension
	return gridTraveler (m - 1, n) + gridTraveler(m, n - 1);
}



// Memoization solution
const gridTraveler_dp = (m, n, memo = {}) => {
	const key = m + ',' + n;
	if (key in memo) return memo[key]
	if (m === 1 && n === 1) return 1;   // 1x1 grid
	if (m === 0 || n === 0) return 0;	// 0x0 grid or false dimension

	memo[key] = gridTraveler_dp (m - 1, n, memo) + gridTraveler_dp (m, n - 1, memo);
	return memo [key];
}





// Driver code
console.log (gridTraveler_dp (1,1));
console.log (gridTraveler_dp (2,3));
console.log (gridTraveler_dp (3,2));
console.log (gridTraveler_dp (3,3));
console.log (gridTraveler_dp (18,18));
