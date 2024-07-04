#!/bin/bash
kill $(pgrep python3)
cd flask_app
python3 -m venv venv
source venv/bin/activate
pip install Flask
cd /home/dima/git2/dima2/
git pull http://root:glpat-zRicZ4WpsXD_pLWb7xAw@192.168.50.147/alo/dima2.git
python3 server1.py
