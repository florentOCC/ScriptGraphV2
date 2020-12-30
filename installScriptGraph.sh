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
