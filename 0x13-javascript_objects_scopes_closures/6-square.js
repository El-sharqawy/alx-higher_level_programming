#!/usr/bin/node

const Square = require('./5-square');

class NewSquare extends Square {
  constructor(size) {
    super(size);
    this.size = size;
  }

  charPrint(char) {
    const newChar = 'X';
    if (!char) {
      char = newChar;
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(char);

        if (j == this.size - 1) {
          process.stdout.write('\n');
        }
      }
    }
  }
}

module.exports = NewSquare;
