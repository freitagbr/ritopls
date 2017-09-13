#!/usr/bin/env bash

for f in *.js
do
  highlight -O rtf -t 2 -K 8 -k 'Roboto Mono' --syntax=js --style $1 $f > "${f%.js}.rtf"
done
