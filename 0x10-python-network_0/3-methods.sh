#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI 7be30073c173.0bc3c855.hbtn-cod.io:5000 | grep "Allow" | cut -d' ' -f2-
