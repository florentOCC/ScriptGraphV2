#!/bin/bash

if [ -z "$(ls /bin | grep python2)" ] 
then
	echo ""
	echo "Installation de Python"
	echo ""
	yum -y install python
	echo ""
else
	echo ""
        echo "Python present"
	echo ""
fi

if [ -z "$(ls /bin | grep pip2)" ]
then
	echo ""
	echo "Installation de pip"
	echo ""
        yum -y install python2-pip
	echo ""	
else
	echo ""
        echo "Pip present"
	echo ""
fi

if [ -z "$(pip list | grep mysql-connector)" ]
then
	echo ""
	echo "Installation connecteur Python-Mysql"
        echo ""
	pip install mysql-connector-python
	echo ""
else
	echo ""
	echo "Connecteur Python-Mysql present"
	echo ""
fi

if [ -z "$(ls /bin | grep ^dot$)" ] 
then
	echo ""
	echo "Installation de Graphviz"
	echo ""
	yum -y install graphviz
	echo ""
else
	echo ""
        echo "Graphviz present"
	echo ""
fi

mkdir /usr/share/ombutel/www/graph
mv index.php /usr/share/ombutel/www/graph/index.php
mv script.php /usr/share/ombutel/www/graph/script.php
mv .htpasswd /usr/share/ombutel/www/graph/.htpasswd
mv .htaccess /usr/share/ombutel/www/graph/.htaccess
echo "apache ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
chmod +x graphV2.py
