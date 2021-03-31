#!/bin/bash

Version1="1.0.0"
Version2="1.0.1"

if [ -z "$(ls | grep ScriptGraphV2-main )" ] 
then
	unzip main.zip
	rm -rf main.zip
	cd ScriptGraphV2-main
	chmod +x installScriptGraph.sh 
	./installScriptGraph.sh
else
	Version1=$(cat ScriptGraphV2-main/Version | cut -d ":" -f 2)
	Version2=$(unzip -p main.zip ScriptGraphV2-main/Version | cut -d ":" -f 2)
	if [ $Version1 != $Version2 ]
	then
		echo "Mise a jour en cours"
		rm -rf ScriptGraphV2-main
		rm -rf /usr/share/ombutel/www/graph
		unzip main.zip
		rm -rf main.zip
		cd ScriptGraphV2-main
		chmod +x installScriptGraph.sh 
		./installScriptGraph.sh
		echo "mise a jour termine !"
	else
		echo "Logiciel deja a jour !"
		rm -rf main.zip
	fi
fi