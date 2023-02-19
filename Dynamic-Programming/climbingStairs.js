// Climbing Stairs

const climbingStairs  = (n) => {
	if (n <= 1) return 1;

	return climbingStairs(n-1) + climbingStairs (n-2);
}




// Memoization
const climbingStairs_dp = (n, memo = {}) => {
	if (n in memo) return memo[n];

	if (n === 1 || n === 0) return 1;
	if (n < 0) return 0;
	memo[n] = climbingStairs_dp (n-1, memo) + climbingStairs_dp(n-2, memo);

	return memo [n];
}


// Driver code
console.log (climbingStairs_dp (3));
console.log (climbingStairs_dp (7));
console.log (climbingStairs_dp (8));
console.log (climbingStairs_dp (50));
