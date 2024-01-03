#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];
const idURL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const allMovies = JSON.parse(body).results;
    let idMovies = 0;

    allMovies.forEach(movie => {
      if (movie.characters.includes(idURL)) {
        idMovies++;
      }
    });

    console.log(idMovies);
  } else {
    console.log(`HTTP error. Status code: ${response.statusCode}`);
  }
});
