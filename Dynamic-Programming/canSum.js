// Write a funciton canSum that takes in a targetSum and an array of numbers as arguments
// The funciton should return a boolean to indicate whether it is 
// possible to generate the targetSum using numbers from the array
// You can use an element as many times as you want

// Brute Force Solution
const canSum = (targetSum, numbers) => {
	if (targetSum === 0) return true;
	if (targetSum < 0) return false;

	for (let num of numbers){
		if (canSum (targetSum - num, numbers)) return true;
	}

	return false;
}


// Optimized Solution
const canSum_dp = (targetSum, numbers, cache = {}) => {
	if (targetSum in cache) return cache [targetSum];
	if (targetSum === 0) return true;
	if (targetSum < 0) return false;
	

	for (let num of numbers){
		if (canSum_dp (targetSum - num, numbers, cache)){
			cache [targetSum] = true;
			return true;
		}
	}
	cache [targetSum] = false;
	return false;

}


// Driver Code
console.log (canSum_dp (7, [2, 3]));
console.log (canSum_dp (7, [5, 3, 4, 7]));
console.log (canSum_dp (7, [2, 4]));
console.log (canSum_dp (8, [2, 3, 5]));
console.log (canSum_dp (300, [7, 14]));
