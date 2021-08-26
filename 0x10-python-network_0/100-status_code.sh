#!/bin/bash
# Sends request to URL arg and displays status code of response
curl "$1" -w '%{http_code}' -so /dev/null
