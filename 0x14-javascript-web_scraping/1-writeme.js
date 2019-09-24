#!/usr/bin/node
const fd = require('fs');
const cb = (err) => {
  if (err) {
    console.error(err);
  }
};
fd.writeFile(process.argv[2], process.argv[3], 'utf-8', cb);
