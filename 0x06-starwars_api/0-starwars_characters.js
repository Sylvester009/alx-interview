#!/usr/bin/env node

const request = require('request');

// Function to make request as a promise
const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(`Status code: ${response.statusCode}`);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

// Main logic
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

requestPromise(apiUrl)
  .then((data) => {
    const characters = data.characters;

    return Promise.all(
      characters.map((url) => requestPromise(url))
    );
  })
  .then((characterData) => {
    characterData.forEach((character) => {
      console.log(character.name);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
  });
