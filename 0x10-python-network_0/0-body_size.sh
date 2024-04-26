#!/bin/bash
# a Bash script that sends request to URL and prints the size of respons's body
curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}'
