#!/bin/bash
#Takes in a URL and displays all HTTP methods the server will accept.
curl -o /tmp/null -sIw %{http_code} $1
