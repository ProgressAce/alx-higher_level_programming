#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie.
 *
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of
 * the list “characters” in the /films/ response.
 * The Star Wars API is used. */

const process = require('process');
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Incorrect usage of program.\n' +
                'USAGE: ./<programName> movieIdOfStarWarsApi');
  process.exit(-1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) { console.error(error); }

  if (response.statusCode === 200) {
    const movie = body;
    // movie = a dictionary of info about the specific movie

    console.log(movie.characters);

    for (const character of movie.characters) {
      // character is a string of a url of the star wars api
      // pointing to the specific character's details
      console.log(character);

      // asynchronous so code goes on while this function processes	    
      request(character, { json: true }, (error, response, body) => {
        if (error) { console.error(error); }

        // body = details about a specific character

        if (response.statusCode === 200) {
  //        const name = body.name;
//          console.log(name);
        }
      });
    }
  }
});
