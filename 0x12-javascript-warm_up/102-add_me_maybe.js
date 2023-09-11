#!/usr/bin/node
// Defines a function that increment the passed arg and calls passed function

exports.addMeMaybe = (number, theFunction) => {
  number++;
  return theFunction(number);
};
