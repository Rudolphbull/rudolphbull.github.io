var logo = document.querySelector('.container');

var menu = document.querySelector('.menu');

logo.addEventListener('click', function(){
    menu.classList.toggle('showmenu');
})

var myFirstName = prompt('What is your name? ');
var firstLetter = myFirstName.slice(0,1);
var firstLetterToUpperCase = firstLetter.toUpperCase();
var remainChar = myFirstName.slice(1,myFirstName.length);
var remainCharToLowerCase = remainChar.toLowerCase();

alert('Hello ' + firstLetterToUpperCase + remainCharToLowerCase);