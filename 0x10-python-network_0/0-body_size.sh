#!/bin/bash
# cURL request that displays size of the response's body
curl -so /dev/null "$1" -w '%{size_download}\n'
