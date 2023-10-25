#!/usr/bin/node
/* Prints the number of movies where the character “Wedge Antilles” is present.
 *
 * The first argument is the API URL of the Star wars API:
 *     https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - this ID is used for filtering
 * the result of the API */

const process = require('process');
const request = require('request');

if (process.argv.length !== 3) {
  console.log('USAGE: ./<program_name> star_wars_API_url');
  process.exit(-1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) { throw error; }

  // all the films in a list of dictionaries
  const movies = JSON.parse(body).results;
  // movies = a list of movies, each movie having a dictionary of its details

  let movieCount = 0;
  for (const movie of movies) {
    for (const character of movie.characters) {
      // character = string url pointing to specific character listed by the api

      if (character.includes(`${18}`)) {
        movieCount += 1;
      }
    }
  }

  console.log(movieCount);
});
