#!/usr/bin/node
const { argv } = require('process');
if (!argv[3]) {
  console.log(0);
} else if (argv[2] && argv[3]) {
  const uniq = [...new Set(argv)];
  function compare (a, b) {
    return (a - b);
  }
  uniq.sort(compare);
  const number = uniq.length;
  console.log(parseInt(uniq[number - 2]));
}
