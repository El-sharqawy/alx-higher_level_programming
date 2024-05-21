#!/usr/bin/node
const fs = require('node:fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url).pipe(fs.createWriteStream(filePath));
