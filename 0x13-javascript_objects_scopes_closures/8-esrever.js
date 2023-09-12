#!/usr/bin/node
// Creates a function that returns the reversed version of a list.

exports.esrever = function (list) {
  let length = list.length - 1;

  for (let i = 0; i < list.length / 2; i++) {
    const temp = list[i];
    list[i] = list[length];
    list[length] = temp;

    length--;
  }

  return list;
};
