#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('0');
} else {
  let max = 0;
  let smax = 0;
  const nums = process.argv.slice(2);
  let num;
  for (num of nums) {
    num = parseInt(num);
    if (num > max) {
      smax = max;
      max = num;
    } else if ((num > smax) && (num !== max)) {
      smax = num;
    }
  }
  console.log(smax);
}
