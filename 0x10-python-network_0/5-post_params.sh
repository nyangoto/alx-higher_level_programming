#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl "$1" -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
