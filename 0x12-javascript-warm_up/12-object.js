#!/usr/bin/node
// Replaces the myObject's value attribute to 12.
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.value = 89;

console.log(myObject);
