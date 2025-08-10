// Variable with type
let message: string = " Hello friend";
console.log(message);

// Function with type annotations
function add(a: number, b: number): number {
    return a + b;
}
console.log(add(5,3));

// array with type
let numbers: number[] = [1,2,3];

// Object type
type User = {
    id: number;
    name: string;
};

let user: User = {id: 1, name: "Alice"};
console.log(user);