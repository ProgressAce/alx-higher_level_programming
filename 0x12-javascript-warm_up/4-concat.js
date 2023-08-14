#!/usr/bin/node
// Prints the first two arguments passed to it, as: "#arg1 is #arg2"

const process = require('process');
const args = process.argv;

console.log(args[2] + ' is ' + args[3]);
