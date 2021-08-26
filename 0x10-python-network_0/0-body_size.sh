#!/bin/bash
# cURL request that displays size of the response's body

curl -so /dev/null -w %{size_download}"\n" "$1"
