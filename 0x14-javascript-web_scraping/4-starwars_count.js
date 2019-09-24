#!/usr/bin/node
const request = require('request');
const f = (error, response, code) => {
  if (error) { console.log(error); }
  let tmp; let cont = 0;
  for (const obj of JSON.parse(response.body).results) {
    const url = '/18/';
    tmp = obj.characters.filter(urlTest => urlTest.includes(url));
    cont = cont + tmp.length;
  }
  console.log(cont);
};
const url = process.argv[2];
request(url, f);
