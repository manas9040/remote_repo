var h1=document.querySelector('h1')
// var p=document.querySelector('p')
// var h2=document.querySelector('h2')
// var ul=document.querySelector('ul')
// var body=document.querySelector('body')

function randomColors(){
  var letters='0123456789ABCDEF'
  var colors='#'
  for (var i = 0; i < 6; i++) {
    var random=Math.floor(Math.random()*16)
    colors=colors+letters[random]
    }
  return colors
}

// function backgroundColor(){
// body.style.background=randomColors()
// }
// setInterval(backgroundColor,5000)

function setColors(){
h1.style.color=randomColors()
// p.style.color=randomColors()
// h2.style.color=randomColors()
// ul.style.color=randomColors()
}
setInterval(setColors,1000)
