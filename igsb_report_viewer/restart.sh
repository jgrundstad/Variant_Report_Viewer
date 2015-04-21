echo mysql login - 
mysql -uroot -p < restart.sql
rm -r viewer/migrations
python manage.py migrate
echo Create jgrundst superuser - 
python manage.py createsuperuser --username=jgrundst --email=jgrundstad@gmail.com 

