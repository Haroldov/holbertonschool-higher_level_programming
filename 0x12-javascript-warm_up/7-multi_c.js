#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing number of occurrences');
} else {
  const max = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < max; i++) { console.log('C is fun'); }
}
