#!/usr/bin/node
// Script: import a dict and sorts it according to its values.

const dict = require('./101-data').dict;
const newDict = {};

for (const key of Object.keys(dict)) {
  console.log(dict[key]);
}
