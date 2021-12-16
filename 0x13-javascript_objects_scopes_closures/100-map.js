#!/usr/bin/node
const list1 = require('./100-data').list;
console.log(list1);
let index = 0;
const map1 = list1.map(function (x) {
  return (x * index++);
});
console.log(map1);
