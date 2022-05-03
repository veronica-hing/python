/* 
Acronyms
Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 
Do it with .split first if you need to, then try to do it without

    - create a function that takes in a string
    - create a returnString var
    - take first char of string and capitalize and push to returnString
    - loop through the string
        - look for the first character after a space
        - capitalize the current char
        - add char to returnString
    - return returnString
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acro(stringy){ //declare function
    //split string into substrings
    let words = stringy.split(" ");// we now have an array with words
    let capAcro = "";//empty string to populate
    //goes through each word in the words array
    for(let i = 0; i < words.length; i++){
        //words[i] gets the word, charAt(0) gets first letter, toUpper() acts on first letter to make it capitalized
        // += appends letter we modified to capAcro
        capAcro += words[i].charAt(0).toUpperCase();
    }
    return capAcro;
}
//console.log to view result of acro when called with str4
console.log(acro(str4));

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {}

// *********************************************

/* 
String: Reverse
Given a string,
return a new string that is the given string reversed
*/

const two_str1 = "creature";
const two_expected1 = "erutaerc";

const two_str2 = "dog";
const two_expected2 = "god";

const two_str3 = "hello";
const two_expected3 = "olleh";

const two_str4 = "";
const two_expected4 = "";

function strRev(stringy){//declar function to reverse string
    //we put the string into an array
    let strArr = stringy.split("");//splitting it so pass in empty string
    //empty str to populate in for loop
    let backwards = "";//creat var to hold new string
    //we get the string and count backwards in the loop
    for(let i = strArr.length - 1; i >= 0; i--){
        backwards += strArr[i];
    }
    return backwards;
}

console.log(strRev(two_str1))
console.log(strRev(two_str4))
/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {}//oops we made a different one