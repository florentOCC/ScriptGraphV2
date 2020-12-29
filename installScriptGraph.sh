#!/bin/bash

if [ -z "rpm -q python" ] 
then
	echo "Installation de Python"
	yum -y install python
else
        echo "Python present"
fi

if [ -z "ls /bin | grep pip" ]
then
	echo "Installation de pip"
        yum -y install python2-pip
else
        echo "Pip present"
fi

if [ -z "pip list | grep mysql-connector" ]
then
	echo "Installation connecteur Python-Mysql"
        pip install mysql-connector-python
else
	echo "Connecteur Python-Mysql present"
fi
