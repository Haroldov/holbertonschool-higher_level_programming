#!/usr/bin/nodejs
const fd = require('fs');
cb = (err, data) => {
    if (err) {
      console.error(err)
    } else {
      process.stdout.write(data)
    }
}
txt = fd.readFile(process.argv[2], 'utf-8', cb)
