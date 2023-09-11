#!/usr/bin/node
// Executes a function x times.

exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
