#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && !isNaN(h) && w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = 'X';
      for (let j = 1; j < this.width; j++) { /* Can also use `repeat()` method */
        x += 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
