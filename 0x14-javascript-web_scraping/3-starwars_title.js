#!/usr/bin/node
const request = require('request');
const ep = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ep}`;

request(url, (err, res, body) => {
  if (err) throw err;

  if (res.statusCode === 200) {
    const resultsJson = JSON.parse(body);
    console.log(resultsJson.title);
  }
});
