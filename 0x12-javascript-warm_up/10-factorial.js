#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return factorial(n - 1) * n;
}

const n = process.argv[2];
let resp;
if (isNaN(parseInt(n)) === true) {
  resp = 1;
} else {
  resp = factorial(n);
}
console.log(resp);
