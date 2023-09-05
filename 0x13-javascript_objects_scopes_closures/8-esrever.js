#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let length = list.length - 1;
  while (i < list.length / 2) {
    const temp = list[i];
    list[i] = list[length];
    list[length] = temp;
    i++;
    length--;
  }

  return list;
};
