#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

const process = require('process');
const args = process.argv;

let largest = args[2]; // first arg
let secondLargest = args[3];

for (let x = 2; x < args.length; x++) {
  if (args[x] > largest) {
    secondLargest = largest;
    largest = args[x];
  } else if (args[x] > secondLargest && args[x] !== largest) {
    secondLargest = args[x];
  }
}

if (args.length < 4) {
  console.log(0);
} else {
//  console.log('largest: ', largest);
  console.log(secondLargest);
}
