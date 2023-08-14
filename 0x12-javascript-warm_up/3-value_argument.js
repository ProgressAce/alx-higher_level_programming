#!/usr/bin/node
// Prints the first passed argument of the js file

const process = require('process');
const args = process.argv;

if (!args[2]) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
