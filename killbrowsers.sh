#!/bin/bash

killall -9 xdg-email

for x in `ps aux | grep chrom | grep -v grep | sed "s/ \+/ /g" | cut -d' ' -f2`; do
   kill -9 $x
done
