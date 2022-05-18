/*
Given an array of strings words, return the words that can be typed using letters of the 
alphabet on only one row of American keyboard like the image below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:
Input: words = ["omk"]
Output: []
Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"] 
*/
//var firstRow = ["q","w","e","r","t","y","u","i","o","p"]
//var secondRow = ["a","s","d","f","g","h","j","k","l"]
//var thirdRow = ["z","x","c","v","b","n","m"]



var findWords = function (words) {
    var one = 'qwertyuiop'
    var two = 'asdfghjkl'
    var three = 'zxcvbnm'
    var newA = []
    var newRow = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for (let word of words) {
        for (let row of newRow) {
            var rowValid=true
            for (let i=0; i<word.length;i++){
                if(!row.includes(word.charAt(i).toLowerCase())) {
                    rowValid=false
                    break

                }
            }
            if (rowValid){
                newA.push(word)
                break
            } 
        } 
        
        // if (one.includes(words[index])) {
        //     newA.push(words[index])
        // }
        // if (two.includes(words[index])) {
        //     newA.push(words[index])
        // }
        // if (three.includes(words[index])) {
        //     newA.push(words[index])


        // } return newA


    }
return newA

}



console.log(findWords(["Hello", "Alaska", "Dad", "Peace"]))
console.log(findWords(["omk"]))
console.log(findWords(["adsdf", "sfd"]))