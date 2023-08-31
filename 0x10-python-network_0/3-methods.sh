#!/usr/bin/env bash
# displays all HTTP methods the URL server will accept.
curl -sI "$1" | grep Allow | cut -d " " -f 2-4
