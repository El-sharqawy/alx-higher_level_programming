#!/usr/bin/node

const fs = require('node:fs');

const content = process.argv[3];

fs.writeFileSync(process.argv[2], content, { encoding: 'utf8', flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
  console.log(content);
});
