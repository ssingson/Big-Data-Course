#!/bin/sh
../start.sh

echo 'This is a test'
read $test

echo What is happening This is happening $test
../stop.sh
