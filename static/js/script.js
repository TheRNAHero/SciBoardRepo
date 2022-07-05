var title=document.getElementById('title')
var name=document.getElementById('name')
var body=document.getElementById('body')

function countChars(obj, num){
    strlength=obj.value.length
    if(strlength>num){
        alert("Max char count is " + num)
        obj.value=obj.value.slice(0, num)
    }
}
