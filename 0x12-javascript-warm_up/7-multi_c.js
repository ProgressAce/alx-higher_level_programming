#!/usr/bin/node
// Prints x times "C is fun".

const process = require('process'); // import 'process'
const args = process.argv;
const num = parseInt(args[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
