/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };

  const keys3 = ["abc", 3, "yo", "something"];
  const vals3 = [42, "wassup", true];
  const expected3 = {
    abc: 42,
    3: "wassup",
    yo: true,
    something: ''
  };

  const keys4 = ["abc", 3, "yo"];
  const vals4 = [42, "wassup", true, "something"];
  const expected4 = false
  
  const keys2 = [];
  const vals2 = [];
  const expected2 = {};
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */



function zipArraysIntoMap(keys, values) {
    //   if there are more values than keys, do not make array, return false
    if(keys.length < values.length){
        return false
    }
    // make a dictionary to hold the key value pairs
    let newDict = {}

    // start for loop to go through array keys to do the assignment to dictionary
    for(let i = 0; i < keys.length; i++){
      // inside the loop, before adding key/value pair, if the value doesn't exist, set an empty string as value for key
        if(values[i]){
            newDict[keys[i]] = values[i]
        }
        else{
            newDict[keys[i]] = ""
        }
    }
    // return dictionary 
    return newDict

  }

  console.log(zipArraysIntoMap(keys1, vals1))
  console.log(zipArraysIntoMap(keys2, vals2))
  console.log(zipArraysIntoMap(keys3, vals3))
  console.log(zipArraysIntoMap(keys4, vals4))
