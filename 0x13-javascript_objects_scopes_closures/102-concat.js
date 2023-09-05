#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fs.existsSync(fileA) && fs.statSync(fileA).isFile && fs.existsSync(fileB) && fs.statSync(fileB).isFile && fileC !== undefined) {
  const fAContent = fs.readFileSync(fileA);
  const fBContent = fs.readFileSync(fileB);
  const stream = fs.createWriteStream(fileC);

  stream.write(fAContent);
  stream.write(fBContent);
  stream.end();
}
