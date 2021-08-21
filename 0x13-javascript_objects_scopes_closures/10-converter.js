#!/usr/bin/node
// Converts number from Base10 to given base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
