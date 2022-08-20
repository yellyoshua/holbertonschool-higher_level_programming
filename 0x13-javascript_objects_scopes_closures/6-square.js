#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    const x = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
};
