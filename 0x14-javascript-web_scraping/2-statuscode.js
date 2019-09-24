x#!/usr/bin/node
const request = require('request');
f = (error, response, code) => {
    console.log('code:', response && response.statusCode);
}
request(process.argv[2], f)
