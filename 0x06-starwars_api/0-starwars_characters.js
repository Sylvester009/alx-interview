#!/usr/bin/node

// Import 'request' module for making HTTP request
const request = require('request');

// Function to make request as a promise
const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject('Status code:' +  response.statusCode);
      } else {
        // Parse JSON
        resolve(JSON.parse(body));
      }
    });
  });
};

// Main logic
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Fetch the movie data
requestPromise(apiUrl)
  .then((data) => {
    const characters = data.characters;

    // Make requests for all characters in parallel using Promise.all
    return Promise.all(characters.map((url) => requestPromise(url)));
  })
  // Extract and print character names
  .then((characterData) => {
    characterData.forEach((character) => {
      console.log(character.name);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
  });
