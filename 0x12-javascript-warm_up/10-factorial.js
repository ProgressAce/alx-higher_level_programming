#!/usr/bin/node
// Computes and prints a factorial

const x = parseInt(process.argv[2], 10);

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }

  return factorial(num - 1) * num;
}

console.log(factorial(x));
