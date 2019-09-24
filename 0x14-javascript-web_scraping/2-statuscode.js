#!/usr/bin/node
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode);
};
request(process.argv[2], f);
