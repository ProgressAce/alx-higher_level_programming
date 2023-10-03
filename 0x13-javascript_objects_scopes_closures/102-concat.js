#!/usr/bin/node
// Concatenates two files.
// the files are passed as args and the third arg is the name of the file
// the File System module is used to read from and write to the files.

const fs = require('fs');

const buffer = fs.readFileSync(process.argv[2]);
const fileContent1 = buffer.toString();

const buffer2 = fs.readFileSync(process.argv[3]);
const fileContent2 = buffer2.toString();

fs.writeFile(process.argv[4], fileContent1 + fileContent2, (err) => {
  if (err) throw err;
});
