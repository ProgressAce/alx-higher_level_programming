#!/usr/bin/node
//

function fact (x) {
  const num = parseInt(x, 10);
  if (num === 0 || isNaN(num)) {
    return 1;
  }

  return num * fact(num - 1);
}

const process = require('process');
const args = process.argv;

console.log(fact(args[2]));
