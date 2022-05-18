/* Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 */

function isSubsequence(s, t) {
    tList=t.split("")

    for(var i=0;i<tList.length;i++){
        if (s.includes(tList[i])){ 
        } 
        else {tList.splice(i,1)}

    }
  let new_set= new Set(tList);


   let new_text=[...new_set].join("");
   console.log(new_text);
    if (new_text == s)
    {return true}
    else{return false}
}


console.log(isSubsequence("abc", "ahbgbdc"))
console.log(isSubsequence("axc", "ahbgdc"))