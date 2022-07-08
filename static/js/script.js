var title=document.getElementById('title')
var name=document.getElementById('name')
var body=document.getElementById('body')
const byteSize = str => new Blob([str]).size;
function countChars(obj, num){
    strlength=byteSize(obj.value)
    console.log(strlength)
    if(strlength>num){
        alert("Max char count is " + num)
        obj.value="Char Limit"
    }
}
