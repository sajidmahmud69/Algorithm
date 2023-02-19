// Fibonacci Sequence

const fib  = (n) => {
	if (n <= 1) return 1;

	return fib(n-1) + fib (n-2);
}




// Memoization
const fib_dp = (n, memo = {}) => {
	if (n in memo) return memo[n];

	if (n <= 1) return 1;
	memo[n] = fib_dp (n-1, memo) + fib_dp(n-2, memo);

	return memo [n];
}


// Driver code
console.log (fib_dp (6));
console.log (fib_dp (7));
console.log (fib_dp (8));
console.log (fib_dp (50));

