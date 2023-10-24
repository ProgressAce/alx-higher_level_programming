#!/usr/bin/node
/* Prints the title of a Star Wars movie where the episode number matches the given integer.
 *
 * The first argument is the movie ID.
 * The Star Wars API with the endpoint  https://swapi-api.alx-tools.com/api/films/:id */

const process = require('process');
const request = require('request');

if (process.argv.length !== 3) {
  console.log('USAGE: ./<program_name> movie_id');
  process.exit();
}

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) { throw error; }

  const movieTitle = JSON.parse(body).title;
  console.log(movieTitle);
});
