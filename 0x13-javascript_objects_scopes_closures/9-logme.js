#!/usr/bin/node
// Prints the number of args already printed and the new arg value.

let argNum = 0;

exports.logMe = function (item) {
  console.log(`${argNum}: ${item}`);
  argNum++;
};
