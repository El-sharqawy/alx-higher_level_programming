#!/usr/bin/node

const X = parseInt(process.argv[2]);
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    for (let j = 0; j < X; j++) {
      process.stdout.write('X');
      if (j === X - 1) {
        process.stdout.write('\n');
      }
    }
  }
}
