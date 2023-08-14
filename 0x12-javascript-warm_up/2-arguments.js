#!/usr/bin/node
const process = require('process');
const args = process.argv;
const argLength = args.length;

if (argLength === 2) {
  console.log('No argument');
} else if (argLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
