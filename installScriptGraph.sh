#!/bin/bash

if [ -z "$(ls /bin | grep python3)" ] 
then
	echo ""
	echo "Installation de Python3"
	echo ""
	yum -y install python3
	echo ""
else
	echo ""
        echo "Python present"
	echo ""
fi

if [ -z "$(ls /bin | grep pip3)" ]
then
	echo ""
	echo "Installation de pip"
	echo ""
        yum -y install python3-pip
	echo ""	
else
	echo ""
        echo "Pip present"
	echo ""
fi

if [ -z "$(pip3 list | grep PyMySQL)" ]
then
	echo ""
	echo "Installation connecteur Python-Mysql"
        echo ""
	pip3 install PyMySQL
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

rm -rf main.zip
mkdir /usr/share/ombutel/www/graph
mv index.php /usr/share/ombutel/www/graph/index.php
mv script.php /usr/share/ombutel/www/graph/script.php
mv .htpasswd /usr/share/ombutel/www/graph/.htpasswd
mv .htaccess /usr/share/ombutel/www/graph/.htaccess
echo "apache ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
chmod +x graphV2.py
