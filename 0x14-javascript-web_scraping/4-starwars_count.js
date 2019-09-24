#!/usr/bin/node
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  let tmp; let cont = 0;
  for (const obj of JSON.parse(response.body).results) {
    const url = 'https://swapi.co/api/people/18/';
    tmp = obj.characters.filter(urlTest => url === urlTest);
    cont = cont + tmp.length;
  }
  console.log(cont);
};
const url = process.argv[2];
request(url, f);
