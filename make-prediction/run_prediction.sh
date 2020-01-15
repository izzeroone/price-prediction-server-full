#!/bin/bash
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
/home/zerotwosdev/miniconda3/envs/tfs/bin/python /home/zerotwosdev/server/cron/create_file.py
/home/zerotwosdev/miniconda3/envs/tfs/bin/python /home/zerotwosdev/server/make-prediction/price_production.py
/home/zerotwosdev/miniconda3/envs/tfs/bin/python /home/zerotwosdev/server/make-prediction/zipped_file.py