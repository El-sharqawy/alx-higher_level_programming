#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    if (!size || size <= 0) {
      return;
    }
    super(Rectangle);
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
