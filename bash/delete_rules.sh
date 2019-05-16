#!/bin/bash

while read CMD; do
    echo $CMD
    rucio delete-rule --purge-replicas --account eschanet $CMD
done
