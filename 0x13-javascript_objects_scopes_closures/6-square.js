#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const { width, height } = this;
    for (let i = 0; i < height; i++) {
      let concat = '';
      for (let j = 0; j < width; j++) {
        concat += c;
      }
      console.log(concat);
    }
  }
} module.exports = Square;
