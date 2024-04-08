#!/usr/bin/node

let myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('No a number');
} else {
  console.log(`My number: ${myVar}`);
}
