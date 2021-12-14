#!/usr/bin/node
const { argv } = require('process');
if (!argv[3]) {
  console.log(0);
} else {
  argv.sort();
  const len = argv.length;
  console.log(argv[len - 2]);
}
