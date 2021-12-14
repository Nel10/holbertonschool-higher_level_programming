#!/usr/bin/node
exports.logMe = ((val = 0) => function (item) {
  console.log(`${val++}: ${item}`);
})();
