#!/bin/bash

Version1="1.0.0"
Version2="1.0.1"

if [ -z "$(ls | grep ScriptGraphV2-main )" ] 
then
	wget https://github.com/florentOCC/ScriptGraphV2/archive/main.zip
	unzip main.zip
	rm -rf main.zip
	cd ScriptGraphV2-main
	chmod +x installScriptGraph.sh 
	./installScriptGraph.sh
else
	Version1=$(curl https://raw.githubusercontent.com/florentOCC/ScriptGraphV2/main/Version | cut -d ":" -f 2 )
	Version2=$(cat ScriptGraphV2-main/Version | cut -d ":" -f 2)
	if [ $Version1 != $Version2 ]
	then
		echo "Mise a jour en cours"
		rm -rf ScriptGraphV2-main
		rm -rf /usr/share/ombutel/www/graph
		wget https://github.com/florentOCC/ScriptGraphV2/archive/main.zip
		sleep 2
		unzip main.zip
		rm -rf main.zip
		cd ScriptGraphV2-main
		chmod +x installScriptGraph.sh 
		./installScriptGraph.sh
		echo "mise a jour termine !"
	else
		echo "Logiciel deja a jour !"
	fi
fi
