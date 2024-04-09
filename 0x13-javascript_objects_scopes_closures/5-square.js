#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(Rectangle);
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
