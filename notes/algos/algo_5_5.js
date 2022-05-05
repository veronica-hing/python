    /* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
        - palindrome = string that is same forwards and backwards
    
    Do not ignore spaces, punctuation and capitalization
    */

    const str1 = "a x a";
    const expected1 = true;
    
    const str2 = "racecar";
    const expected2 = true;
    
    const str3 = "Dud";
    const expected3 = false;
    
    const str4 = "oho!";
    const expected4 = false;
    
    const str5 = "rats live on no evil star";
    //   const expected5 = true;
    
    /**
     * Determines if the given str is a palindrome (same forwards and backwards).
     * - Time: O(?).
     * - Space: O(?).
     * @param {string} str
     * @returns {boolean} Whether the given str is a palindrome or not.
     */

    function isPalindrome(str) {
        //for loop that goes through str
        for(let i = 0; i < str.length/2; i++){//only need to check halfway since going from end as well
            //inside string, if statement checks first and last, then second and second to last ..
            if(str[i] === str[str.length - 1 - i] ){
                // -1 to stay inside of str array
                //continue since we're ok
            }else{
                return false
            }
        }  
        return true   
    }
 //   console.log(isPalindrome(str5))
 //   console.log(isPalindrome(str4))

  //  console.log(isPalindrome("tacocat"))
  //  console.log(isPalindrome("borroworrob"))
  //  console.log(isPalindrome("glad you are king"))
  //  console.log(isPalindrome("murder for a jar of redrum"))// good for next palindrome function
  //  console.log(isPalindrome("never odd or even"))// also good for next one


    /* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided,
    but also at the substrings within it.
    Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

const two_str5 = "a1001x20002y567765z";
const two_expected5 = "567765";


function isPalindromeSubFunc(str) {
    //for loop that goes through str
    for(let i = 0; i < str.length/2; i++){//only need to check halfway since going from end as well
        //inside string, if statement checks first and last, then second and second to last ..
        if(str[i] === str[str.length - 1 - i] ){
            // -1 to stay inside of str array
            //continue since we're ok
        }else{
          //  console.log(false)
            return false
        }
    }  
    //console.log(true)
    return str  
}
/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    let palindromes = [];
    let temp = "";
    //loop through entire string TWICE
    //first loop goes forward through entire string repeatedly, all, all after second, all after third etc.
    for(let i = 0; i < str.length; i++){
        temp = str.slice(i);
        if(isPalindromeSubFunc(temp)){
            palindromes.push(temp)
        }
    }//we now have array of palindromes
    console.log(palindromes)
    var maxWord = "";
    for(let i = 0; i < palindromes.length - 2; i++){
        if(palindromes[i].length > palindromes[i+1]){
            maxWord = palindromes[i];
        } else{
            maxWord = palindromes[i+1];
        }
    }
    return maxWord;
}

console.log(longestPalindromicSubstring(two_str1))