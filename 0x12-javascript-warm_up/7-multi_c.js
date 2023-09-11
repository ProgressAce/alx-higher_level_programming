#!/usr/bin/node
// Prints "C is fun" x number of times.

const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
