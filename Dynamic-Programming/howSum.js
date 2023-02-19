// Write a function 'howSum (targetSum, numbers)' that takes in a targetSum and array of numbers as arguments
// Return an array containing a combination of elements that add up to exactly
// the targetSum. If there is no combination return an empty array


// Brute Force Solution
const howSum = (targetSum, numbers) => {
	if (targetSum === 0) return [];
	if (targetSum < 0) return null;

	for (let num in numbers){
		const remainder = targetSum - num;
		const sumArray = howSum (remainder, numbers); 
		if (sumArray !== null){
			return [ ...sumArray, num];
		}
	}
	return null;
}


// Optimized Solution
const howSum_dp = (targetSum, numbers, memo = {}) => {
	if (targetSum in memo) return memo [targetSum];
	if (targetSum === 0) return [];
	if (targetSum < 0) return null;

	for (let num in numbers){
		const tempArr = howSum_dp (targetSum - num, numbers, memo);
		if (tempArr !== null){
			memo [targetSum] = [ ...tempArr, num];
			return memo [targetSum];
		}
	}
	memo [targetSum] = null;
	return null;
}





// Driver Code
console.log (howSum_dp (7, [2, 3]));
//console.log (howSum (7, [5, 3, 4]));
//console.log (howSum (7, [2, 4]));
//console.log (howSum (8, [2, 3, 5]))
