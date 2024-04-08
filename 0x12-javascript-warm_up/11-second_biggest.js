#!/usr/bin/node

let x = 0;
for (let i = 0; i <= process.argv.length; i++) {
  if (process.argv[i] > x) {
    x = process.argv[i];
  }
}

console.log(x);
