#!/bin/bash
# a Bash script that displays all the Http methods accepted by server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
