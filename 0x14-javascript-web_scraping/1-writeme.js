#!/usr/bin/node
/* Script that writes a string to a file.
 *
 * The first argument is the path to the file.
 * The second argument is the string to write.
 * The content of the file is written in utf-8.
 * If an error occured while writing, prints the error object. */

const fs = require('fs');
const process = require('process');

if (process.argv.length !== 4) {
  console.log('USAGE: ./<program_name> file_path string');
  process.exit();
}

const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, 'utf-8', function (err) {
  if (err) { throw err; }
});
