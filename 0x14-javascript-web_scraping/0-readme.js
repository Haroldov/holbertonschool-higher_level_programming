#!/usr/bin/node
const fd = require('fs');
const cb = (err, data) => {
  if (err) {
    console.error(err);
  } else {
    process.stdout.write(data);
  }
};
fd.readFile(process.argv[2], 'utf-8', cb);
