#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const printFrequency = parseInt(process.argv[2]);
  for (let i = 0; i < printFrequency; i++) {
    console.log('C is Fun');
  }
}
