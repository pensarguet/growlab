#!/bin/bash
export SENSOR_TYPE=none

export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa"

python3 app.py

cp html/* ../../growlab-livepreview/

cd ../../growlab-livepreview

git add .

git commit -s -m "Update images at `date`"

git pull origin  main --rebase

git push origin main
