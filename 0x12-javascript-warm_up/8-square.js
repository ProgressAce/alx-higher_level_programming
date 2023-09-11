#!/usr/bin/node
// Prints a square to the console.

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let sq = '';

    for (let j = 0; j < size; j++) {
      sq += 'X';
    }
    console.log(sq);
  }
}
