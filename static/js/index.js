let num1 = document.querySelector("#num1");
let num2 = document.querySelector("#num2");
let add = document.querySelector("#add");
let sub = document.querySelector("#sub");
let mul = document.querySelector("#mul");
let div = document.querySelector("#div");
let res = document.querySelector("#result");

add.addEventListener('click', () => {
    let a = parseFloat(num1.value);
    let b = parseFloat(num2.value);
    res.innerHTML = `${a} + ${b} = ${a+b}`;
});

sub.addEventListener('click', () => {
    let a = parseFloat(num1.value);
    let b = parseFloat(num2.value);
    res.innerHTML = `${a} - ${b} = ${a-b}`;
});

mul.addEventListener('click', () => {
    let a = parseFloat(num1.value);
    let b = parseFloat(num2.value);
    res.innerHTML = `${a} x ${b} = ${a*b}`;
});

div.addEventListener('click', () => {
    let a = parseFloat(num1.value);
    let b = parseFloat(num2.value);
    res.innerHTML = `${a} / ${b} = ${a/b}`;
});