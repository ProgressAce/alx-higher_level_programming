#!/usr/bin/node
/* Script that displays the status code of a GET request.
 *
 * The first argument is the URL to request (GET)
 * The status code is printed like this: code: <status code> */

const process = require('process');
const request = require('request');

if (process.argv.length !== 3) {
  console.log('USAGE: ./<program_name> url_to_request');
  process.exit();
}

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { throw error; }

  console.log(`code: ${response.statusCode}`);
});
