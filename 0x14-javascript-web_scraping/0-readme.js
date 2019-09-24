#!/usr/bin/node
const fd = require('fs');
const cb = (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
};
fd.readFile(process.argv[2], 'utf-8', cb);
