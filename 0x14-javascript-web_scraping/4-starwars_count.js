#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];
const id = '18';

request(apiURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const allMovies = JSON.parse(body).results;
    let idMovies = 0;

    allMovies.forEach(movie => {
      movie.characters.forEach(url => {
        if (url.includes(id)) {
          idMovies++;
        }
      });
    });

    console.log(idMovies);
  } else {
    console.log(`HTTP error. Status code: ${response.statusCode}`);
  }
});
