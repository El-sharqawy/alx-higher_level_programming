#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint(char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char);

        if (j == this.width - 1) {
          process.stdout.write('\n');
        }
      }
    }
  }
}

module.exports = Square;
