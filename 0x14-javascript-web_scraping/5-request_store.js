#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file.
 *
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file is encoded in UTF-8 */

const fs = require('fs');
const process = require('process');
const request = require('request');

if (process.argv.length !== 4) {
  console.log('USAGE: ./<program_name> url file_path');
  process.exit();
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) { throw error; }

  const content = body;

  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) { throw error; }
  });
});
