#!/usr/bin/node
const { argv } = require('process');
const printFrequency = parseInt(argv[2]);
if (isNaN(printFrequency)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < printFrequency; i++) {
    console.log('C is fun');
  }
}
