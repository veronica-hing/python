/*
Recursive Factorial
Input: integer
Output: integer, product of ints from 1 up to given integer

If less than zero, treat as zero.
Bonus: If not integer, truncate (remove decimals).

Experts tell us 0! is 1.

rFact(3) = 6 (1*2*3)
rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

/**
* Recursively multiples 1 to the given int.
* - Time: O(?).
* - Space: O(?).
* @param {number} n The int to factorial. Treat negatives as zero and
*    floor decimals.
* @returns {number} The result of !n.
*/
function factorial(n) {
    n = n - n % 1; //floor the input
    if(n <= 1){
        return 1
    }// base case and kind of an edge case when input is 0 
    return n * factorial(--n)
}

//console.log(factorial(num1))
//console.log(factorial(num2))
//console.log(factorial(num3))


// *************************************************************************

/* 
Return the fibonacci number at the nth position, recursively.

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it,
starting with 0 and 1 as the first two numbers of the sequence.
*/

const two_num1 = 0;
const two_expected1 = 0;

const two_num2 = 1;
const two_expected2 = 1;

const two_num3 = 2;
const two_expected3 = 1;

const two_num4 = 3;
const two_expected4 = 2;

const two_num5 = 4;
const two_expected5 = 3;

const two_num6 = 8;
const two_expected6 = 21;

/**
* Recursively finds the nth number in the fibonacci sequence.
* - Time: O(?).
* - Space: O(?).
* @param {number} num The position of the desired number in the fibonacci sequence.
* @returns {number} The fibonacci number at the given position.
*/
function fibonacci(num) {
    //if less than 2, return base case of either 0 or 1
    if(num < 2) return num;
    //take the two numbers before it then add them
    return fibonacci(num-2)+fibonacci(num-1)
}

console.log(fib(two_num1))
console.log(fib(two_num2))
console.log(fib(two_num3))
console.log(fib(two_num4))
console.log(fib(two_num5))
console.log(fib(two_num6))


function fib(num, numObj= {0:0, 1:1}) {
    if(numObj.hasOwnProperty(num)){
        return numObj[num];
    }else{
        //if less than 3, return base case of either 0 or 1
        if(num <0){
            return null
        } 
        if(numObj[num] !== undefined){
            return numObj[num];
        }
    }
    numObj[num] = fib(num - 1, numObj) + fib(num - 2, numObj)
    return numObj[num]
}

