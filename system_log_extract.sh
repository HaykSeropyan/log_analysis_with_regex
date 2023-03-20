#! /bin/bash

>info.txt
>error.txt
echo "start process"

grep INFO syslog.log >> info.txt
grep ERROR syslog.log >> error.txt


echo "done extracting"
