#!/usr/bin/node

function getBiggest () {
  let x = 0;
  if (process.argv.length - 2 === 1) {
    return (x);
  } else {
    for (let i = 0; i < process.argv.length; i++) {
      if (process.argv[i] > x) {
        x = process.argv[i];
      }
    }
  }
  return (x);
}

console.log(getBiggest());
