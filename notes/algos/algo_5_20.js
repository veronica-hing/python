/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [5, 4, 1, 4, 1, 5];
const expected6 = [];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    if (!nums) return nums; //check input before doing work
    //keep track of number of times number shows up by using object since keys must be unique
    //value is the number of times it shows up
    let numsObj = {}
    
    for(let i = 0; i < nums.length; i++){
        if( !numsObj[nums[i]]){
            numsObj[nums[i]] = 1;
        }else{ numsObj[nums[i]]++}
    }//numsObj now has number of instances each key shows up
    
    let max = 0; //1 since key should show up at least once
    let otherMaxes = [];//will check before returning, if empty just return key where value is max
    
    for(let key in numsObj){
        if(numsObj[key] > max){
            max = numsObj[key];
        }
        else if(numsObj[key] === max){
            otherMaxes.push(numsObj[key])
        }
    }//max should be set to highest instance
    //other maxes should be populated with similar higher instances

    //case for only 1 number has mode
    if(otherMaxes.length === 0){
        for(var key in numsObj){
            if(numsObj[key] === max){
                return key //returns actual number
            }
        }
    }
    //case for all numbers show up same number of times
    //+1 on othermaxes since the first max is not included

    if(nums.length === ((otherMaxes.length + 1) * max)){
        return []
    }

    let modeNums = []

    for(key in numsObj){
        if(numsObj[key]=== max){
            modeNums.push(key)
        }
    }
    return modeNums
}

console.log(mode(nums1))
console.log(mode(nums2))
console.log(mode(nums3))
console.log(mode(nums4))
console.log(mode(nums5))
console.log(mode(nums6))

