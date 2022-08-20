#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    return array.concat(current);
  }, []);
};
