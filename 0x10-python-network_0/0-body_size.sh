#!/bin/bash
# cURL request that displays size of the response's body

curl -s $1 -w %{size_download}"\n" -o /dev/null
