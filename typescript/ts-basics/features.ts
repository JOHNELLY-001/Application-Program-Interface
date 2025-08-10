// Creating a program that: Defines and Animal interface 
// create an array of animals 
// A function to filter animals by species


interface Animal {
    id: number;
    name: string;
    species: string;
}

let animals: Animal[] = [
    { id: 1, name: "Cat", species: "Cat"},
    { id: 2, name: "dog", species: "dog"}
];

function filterBySpecies(list: Animal[], species: string): Animal[] {
    return list.filter(a => a.species === species);
}

console.log(filterBySpecies(animals, "dog"));