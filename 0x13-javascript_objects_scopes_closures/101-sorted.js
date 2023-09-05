#!/usr/bin/node
const dict = require('./101-data').dict;

const values = Object.values(dict);
const totList = Object.entries(dict);
const uniqValues = [...new Set(values)];
const newDict = {};
for (const i in uniqValues) {
  const list = [];
  for (const j in totList) {
    if (totList[j][1] === uniqValues[i]) {
      list.unshift(totList[j][0]);
    }
  }
  newDict[uniqValues[i]] = list;
}

console.log(newDict);
