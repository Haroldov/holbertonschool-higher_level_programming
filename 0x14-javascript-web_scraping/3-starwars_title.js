#!/usr/bin/node
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  console.log(JSON.parse(response.body).title)
};
let url = 'http://swapi.co/api/films/'
url = url + process.argv[2]
request(url, f);
