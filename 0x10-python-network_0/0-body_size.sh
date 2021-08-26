#!/bin/bash
# cURL request that displays size of the response's body

curl -s -w %{size_download}"\n" "$1" -o /dev/null
