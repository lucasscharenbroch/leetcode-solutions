#!/bin/bash

sed -n -e '/^([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}$/p' \
       -e '/^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$/p' file.txt