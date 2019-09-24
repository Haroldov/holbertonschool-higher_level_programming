#!/usr/bin/node
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  const dict = {};
  for (const obj of JSON.parse(response.body)) {
    if (dict[obj.userId]) {
      dict[obj.userId] = dict[obj.userId] + 1;
    } else {
      dict[obj.userId] = 1;
    }
  }
  console.log(dict);
};
const url = process.argv[2];
request(url, f);
