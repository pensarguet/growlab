#!/bin/bash
export SENSOR_TYPE=bme680
python3 app.py

export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa"

cp ${HOME}/growlab/app/html/* ${HOME}/growlab/docs/

git add ../docs/index.html
git add ../docs/preview.jpg

git commit -s -m "Update images at `date`"
# git pull origin master --rebase
git push origin master

