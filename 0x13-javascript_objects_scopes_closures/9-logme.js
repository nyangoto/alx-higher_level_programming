#!/usr/bin/node
// Prints number of argumrnts already printed and new value
exports.logMe = function (item) {
  this.times = (this.times || 0) + 1;
  console.log(`${this.times - 1}: ${item}`);
};
