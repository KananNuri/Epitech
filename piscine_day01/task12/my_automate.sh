#!/bin/bash

task_count=$1
day_number=$2

day=$(printf "%02d" "$day_number")

mkdir "day$day"

for i in $(seq 1 "$task_count")
do
    task=$(printf "%02d" "$i")
    mkdir "day$day/task$task"
done
