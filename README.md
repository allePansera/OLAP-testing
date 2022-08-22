# OLAP-testing
Local &amp; Web OLAP testing
Python 3.6.0 is required for current cubes library release.

## Local
Inside /local directory in example directory is located the code to run locally basic aggregation.
Data are stored inside data.csv file in /local directory.

Execution Step:
* cd /local
* pip3 (or python -m pip) install -r requirements.txt
* python3 (or python 4 win10/11 users) prepare_data.py
* python3 (or python 4 win10/11 users) aggregate.py

## Web
Inside /web directory in example directory is located the code to run cubes at 127.0.0.1:5000.
Data are stored inside data.csv file in /local directory.

Execution Step:
* cd /web
* pip3 (or python -m pip) install -r requirements.txt
* python3 (or python 4 win10/11 users) prepare_data.py
* python3 (or python 4 win10/11 users) application.py

## 2ND Local Test
Inside /2nd_local directory in example directory is located the code to run locally basic aggregation.
Data are stored inside export_data_fotografia.csv file in /2nd_local directory.
In order to run the samples the steps are the same for 'local'.


