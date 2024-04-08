#!/usr/bin/node

function getBiggest () {
  let x = 0;
  if (process.argv.length - 2 === 1) {
    return (x);
  } else {
    for (let i = 0; i < process.argv.length; i++) {
      if (parseInt(process.argv[i]) > x) {
        x = praseInt(process.argv[i]);
      }
    }
  }
  return (x);
}

console.log(getBiggest());
