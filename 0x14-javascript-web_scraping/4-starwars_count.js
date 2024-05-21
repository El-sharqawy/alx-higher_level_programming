#!/usr/bin/node
const request = require('request');
const input = process.argv[2];

request(input, (err, res, body) => {
  if (err) throw err;

  const resultJson = JSON.parse(body).results;
  console.log(resultJson.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
