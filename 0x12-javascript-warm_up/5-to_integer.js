#!/usr/bin/node
// Logs "My number: <first argument converted to integer>" to the console

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
