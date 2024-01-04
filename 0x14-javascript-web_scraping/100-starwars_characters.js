#!/usr/bin/node

const request = require('request');
const starWarsURL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(starWarsURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const allCharacters = JSON.parse(body).characters;

    allCharacters.forEach(characterURL => {
      request(characterURL, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
