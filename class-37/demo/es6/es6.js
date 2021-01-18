let num = 9;
// let num = 1;
num = 1;
console.log(num);

const food = 'Shawerma';
// food = 'Falafel';
console.log(food);

const constArray = [];
constArray.push(1);
console.log(constArray);

// constArray = [3,4]; // Error


for(let i=0; i<5; i++){
    let innerVar = i*2;
    // console.log(innerVar);
}

// console.log(innerVar); // Error


// Arrow Functions
function regularMultiply(a, b){
    console.log(a*b);
    console.log(this);
}
regularMultiply(2,3);


const arrowMultiply = (a, b) => {
    console.log(a*b);
    console.log(this);
}
arrowMultiply(2,3);
