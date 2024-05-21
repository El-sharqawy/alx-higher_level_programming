#!/usr/bin/node
const fs = require('node:fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
