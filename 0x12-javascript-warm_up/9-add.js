#!/usr/bin/node
// Prints the addition of two integers

function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}

const process = require('process');
const args = process.argv;

console.log(add(args[2], args[3]));
