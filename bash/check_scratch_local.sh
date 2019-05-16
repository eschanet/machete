#!/bin/bash

if [ $# -lt 1 ]
then
    echo "usage: check_scratch_local.sh hostname"
    exit
fi

node=$1

ssh $node 'mydirs=$(find /scratch-local -maxdepth 1 -user $(id -u));[[ -n $mydirs ]] && du -shc $(echo $mydirs)'
