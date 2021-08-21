#!/usr/bin/node
const dict = require('./101-data').dict;
console.log(Object.entries(dict).reduce(function (i, idx) {
  i[idx[1]] = (i[idx[1]] || []).concat(idx[0]);
  return i;
}, {}));
