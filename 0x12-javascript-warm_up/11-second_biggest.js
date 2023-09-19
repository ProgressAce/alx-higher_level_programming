#!/usr/bin/node
// Searches for the second biggest integer in the list of args.

const args = process.argv;

let largest = args[2];
let secLargest = args[3];

for (const i of args[2:]) {
  console.log(i);
}
