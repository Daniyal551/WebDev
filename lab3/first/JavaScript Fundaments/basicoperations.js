//task1: the postfix and prefix forms
let a=1,b=1;
let c=++a;//a=2;c=2;
let d=b++;//b=2;d=1;

//task2: assignment result
let f=2;
let x=1+(a*=2);//f=4;x=5

//task3: type conversions
"" + 1 + 0//10
"" - 1 + 0//-1
true + false//1
6 / "3"//2
"2" * "3"//6
4 + 5 + "px"//9px
"$" + 4 + 5//$45
"4" - 2//2
"4px" - 2//Nan
"  -9  " + 5//"  -9  5"
"  -9  " - 5//-14
null + 1//1
undefined + 1//Nan
" \t \n" - 2//-2

//task4: fix the addition
let q = +prompt("First number?", 1);
let w = +prompt("Second number?", 2);
//it returns q,w as strings. therefore we add +promot
alert(q+w); // 12