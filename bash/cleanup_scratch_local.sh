#!/bin/bash

for node in $(seq -w 1 99)
do
  [ "$node" -eq 69 ] && continue
  echo "Cleaning etp${node}"
  ssh gar-ws-etp${node} -o ConnectTimeout=2 'mydirs=$(find /scratch-local -maxdepth 1 -user $(id -u));[[ -n $mydirs ]] && chmod -R 755 $(echo $mydirs);[[ -n $mydirs ]] && rm -rf $(echo $mydirs);'
done
