#!/usr/bin/node
const fd = require('fs');
const cb = (err) => {
  if (err) {
    console.error(err);
  }
};
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  fd.writeFile(process.argv[3], response.body, 'utf-8', cb);
};
const url = process.argv[2];
request(url, f);
