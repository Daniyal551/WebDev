//task1: will it be shown?
if ("0") {
    alert( 'Hello' );
  }//it will work because any string except an empty becomes true

//task3: show the sign
let val = prompt('Type a number', 0);

if (val > 0) {
  alert( 1 );
} else if (val < 0) {
  alert( -1 );
} else {
  alert( 0 );
}

//task4: rewrite if
//answer: 
let result=(a+b<4) ? 'Below' : 'Over';

//task5: rewrite if else
let message=(login=='Emplotee') ? 'Hello' :
    (login=='Director') ? 'Greetings' :
    (login=='') ? 'No login' :
    '';
