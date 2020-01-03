#!/bin/bash
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
/home/zerotwosdev/miniconda3/envs/tfs/bin/python /home/zerotwosdev/server/price-prediction-server/manage.py start