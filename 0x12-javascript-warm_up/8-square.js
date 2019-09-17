#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing size');
} else {
  const max = parseInt(process.argv[2]);
  let i, j;
  let str;
  for (i = 0; i < max; i++) {
    str = '';
    for (j = 0; j < max; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
