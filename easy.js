var assert = require("assert")
// Given an array of numbers, return a new array so that positive and negative
// numbers alternate. You can assume that 0 is a positive number. Within the
// positive and negative numbers, you must keep their relative order. You are 
// guaranteed the number of positive and negative numbers will not differ by more 
// than 1.

// =====Example 1
// Input: [1, -3, -8, -5, 10]
// Output: [-3, 1, -8, 10, -5]
// Explanation: We have alternated positive and negative numbers. Notice that the
// negative numbers appear in the same relative order (-3, -8, -5) and the positive
// numbers appear in the same order as well (1, 10).

// =====Example 2
// Input: [3, 0, 0, -5, -2]
// Output: [3, -5, 0, -2, 0]
// Explanation: We have alternated positive and negative numbers. Notice they appear
// in the same relative order.

// =====Example 3
// Input: [0, -3, 3, -1, 1, -1]
// Output #1: [0, -3, 3, -1, 1, -1]
// Output #2: [-3, 0, -1, 3, -1, 1]
// Explanation: There are 2 possible answers which satisfy the problem's constraints.
// We can start with either positive or negative

// =====Example 4
// Input numArray: []
// Output numArray: []
// Explanation: Empty array...

const altNumbers = (numArray) => {
    //NOTE: THE REASON I THINK IT WOULD BE UNHEARD OF TO LOOP THROUGH INPUT AS YOU CREATE OUTPUT IS BECAUSE
    //YOU NEED TO KNOW THE LENGTH OF THE POSITIVE AND NEGATIVE NUMBERS TO DETERMINE WHICH VALUE GOES FIRST
    const pos = [];
    const neg = [];
    for (var i = 0, len = numArray.length; i < len; i++) {
        //neg
        let val = numArray[i];
        if (val < 0) {
            neg.push(val);
        }
        //pos
        else {
            pos.push(val);
        }
    }
    //the pos and neg are split but in order as of right now
    let posLen = pos.length;
    let negLen = neg.length;
    let result = [];
    //NOTE: ONLY NEED TO ADD ONE MORE ELEMENT TO THE RESULT AFTER LOOPS FOR FIRST 2 CASES SINCE WE KNOW
    //POSITIVE AND NEGATIVE ONLY DIFFER BY 1.
    // more positive values then negative, so positive goes first
    if (posLen > negLen) {
        //use neg length and then add one more from positive
        let i = 0;
        while (i < negLen) {
            result.push(pos.at(i));
            result.push(neg.at(i))
            i++;
        }
        //last element of the positive list
        result.push(pos.at(i));
    }

    // negatives goes first, since there are more negativesS
    else if (posLen < negLen) {
        //use pos length then add one more from negative
        let i = 0;
        while (i < posLen) {
            result.push(neg.at(i));
            result.push(pos.at(i))
            i++;
        }
        //last element of the positive list
        result.push(neg.at(i));
        
    }
    //seperated this case, was going to put in else if because the code will look much cleaner then
    //posLen == negLen
    else {
        let i = 0;
        while (i < posLen) {
            result.push(neg.at(i));
            result.push(pos.at(i))
            i++;
        }
    }
    return result;
}

module.exports = { altNumbers } // Do not modify this line

// ====================TESTS====================
// Some tests to help you check your progress. Simply run your code with
// node easy.js
// If successful, no output should appear. If unsuccessful, you should see 
// assertion errors being thrown.

let array1 = [1, -3, -8, -5, 10]
array1 = altNumbers(array1)
const answer1 = [-3, 1, -8, 10, -5]
for (let i = 0; i < array1.length; i++) {
    assert(array1[i] === answer1[i])
}

let array2 = [3, 0, 0, -5, -2]
array2 = altNumbers(array2)
const answer2 = [3, -5, 0, -2, 0]
for (let i = 0; i < array2.length; i++) {
    assert(array2[i] === answer2[i])
}

let array3 = [0, -3, 3, -1, 1, -1]
array3 = altNumbers(array3)
const answer3a = [0, -3, 3, -1, 1, -1]
const answer3b = [-3, 0, -1, 3, -1, 1]
if (array3[0] === 0) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3a[i])
    }
} else if (array3[0] == -3) {
    for (let i = 0; i < array3.length; i++) {
        assert(array3[i] === answer3b[i])
    }
} else {
    assert(false)
}

let array4 = []
array4 = altNumbers(array4)
assert(array4.length === 0)

let array5 = [3,2,1,-1,-2,-3,-4]
array5 = altNumbers(array5)
const answer5 = [-1, 3, -2, 2, -3, 1, -4]
for (let i = 0; i < array5.length; i++) {
    assert(array5[i] === answer5[i])
}

let array6 = [5,-1,-2,-3,-4,0,3]
array6 = altNumbers(array6)
const answer6 = [-1, 5, -2, 0, -3, 3, -4]
for (let i = 0; i < array6.length; i++) {
    assert(array6[i] === answer6[i])
}