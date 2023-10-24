#!/usr/bin/node
/* Script that reads and prints the content of a file.
 *
 * The first argument is the file path.
 * The file content must be read in utf-8.
 * If an error occured during the reading, print the error object. */

const fs = require('fs');
const process = require('process');

if (process.argv.length !== 3) {
  console.log('USAGE: ./<program_name> path_to_file');
  process.exit();
}

const filePath = process.argv[2];
// Read file
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }

  console.log(data);
});
