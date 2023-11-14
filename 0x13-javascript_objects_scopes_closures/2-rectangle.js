#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && !isNaN(h) && w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
