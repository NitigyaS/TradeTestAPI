### WebApp Skeleton
Skeleton to quickly start with a webapp in flask. Its made for saving first 30 minutes of a person.

Code consist of
1. BluePrints
2. Db model using SQLAlchemy
3. Run Script
4. unittest file
5. setup.py
6. requirement
7. config file

#How to start with skeleton

export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run

##How to create nifty
flask db init
flask db migrate
flask db update

## How to load data in nifty table (Untill I convert it in a API Call)
Download file from nse : https://www.nseindia.com/content/indices/ind_nifty50list.csv
remove first line
mv filename.csv nifty.csv
mysql
mysql> use database_name;
mysql> load data local infile 'nifty.csv' into table nifty fields terminated by ',' lines terminated by '\n';
