#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const starwarsURL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(starwarsURL, (err, response, body) => {
  // const bodyJSON = JSON.parse(body)
  console.log(JSON.parse(body).title);
});
