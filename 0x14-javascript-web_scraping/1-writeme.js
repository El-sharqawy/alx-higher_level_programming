#!/usr/bin/node
const fs = require('node:fs');
const fileName = process.argv[2]
const content = process.argv[3]
fs.writeFileSync(fileName, content, { encoding: 'utf8', flag: 'w' }, (err) => {
  if (err) throw err;
});
