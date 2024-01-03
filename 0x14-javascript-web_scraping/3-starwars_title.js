#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const starwarsURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(starwarsURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
