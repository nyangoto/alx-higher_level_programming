#!/usr/bin/node
/* Maps an array and multiplies each element eith it's index */
const list = require('./100-data').list;
console.log(list);
console.log(list.map((element, index) => element * index));
