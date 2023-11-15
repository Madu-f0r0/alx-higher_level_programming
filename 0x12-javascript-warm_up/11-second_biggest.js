#!/usr/bin/node
const { argv } = require('process');
const sortedArr = argv.slice(2).sort(function (a, b) { return (a - b); });
const secondLargest = sortedArr.length > 1 ? sortedArr[sortedArr.length - 2] : 0;
console.log(secondLargest);
