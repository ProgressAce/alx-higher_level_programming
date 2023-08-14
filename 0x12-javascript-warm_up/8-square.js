#!/usr/bin/node
// Prints a square

const process = require('process');
const range = parseInt(process.argv[2], 10);

if (isNaN(range)) {
  console.log('Missing size');
} else {
  let square = '';

  for (let x = 0; x < range; x++) {
    for (let y = 0; y < range; y++) {
      square += 'X';
    }
    if (x < range - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
