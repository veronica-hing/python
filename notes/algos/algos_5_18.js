/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
function dedupeSorted(nums) {
    //add values into dictionary since keys are unique
    if(nums.length <= 1) return nums;
    let numsUniq = {};
    for(let i = 0; i< nums.length; i++){
        if(!numsUniq[nums[i]]){
            numsUniq[nums[i]] = 1;
        }
        //we don't care how many times it shows up
    }
    //take those keys and put them in a new array that gets returned
    let uniqArr = [];
    for(let num in numsUniq){
        uniqArr.push(num);
    }
    return uniqArr
}

console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))
console.log(dedupeSorted(nums4))

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const nums12 = [3, 5,7, 4, 3, 4, 6, 5];
const expected12 = 6;

const nums22 = [3, 5, 5];
const expected22 = 3;

const nums32 = [3, 3, 5];
const expected32 = 5;

const nums42 = [5];
const expected42 = 5;

const nums52 = [];
const expected52 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
    //use a dictionary for putting nums into since keys must be unique
    let numsDict = {};
    //go through input array to start putting things into dict
    for( let i = 0; i < nums.length; i++){
        //initializes the first time we put a number in
        if(! numsDict[nums[i]]){
            numsDict[nums[i]] = 1;
        }// another instance of same number shows up
        else{numsDict[nums[i]] ++}
    }//full dictionary with number as key and how many times it shows up as values
    
    //going through the dictionary WHICH IS UNORDERED
    for (let num of nums){
        //finding where it is 1 instance
        //console.log(num);
        if(numsDict[num] === 1){
            return num;
        }
    }

    return null
}

console.log(firstNonRepeated(nums12))
console.log(firstNonRepeated(nums22))
console.log(firstNonRepeated(nums32))
console.log(firstNonRepeated(nums42))
console.log(firstNonRepeated(nums52))
