#!/bin/bash

DIR="."

for file in "$DIR"/*.py
do
    python "$file" &
done

wait

echo "Ready."

