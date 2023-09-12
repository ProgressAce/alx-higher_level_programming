#!/usr/bin/node
// Creates a class that defines a square and inherits from Square of 5-square.js.

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let shape = '';

      for (let j = 0; j < this.width; j++) {
        shape += c;
      }
      console.log(shape);
    }
  }
}

module.exports = Square;
