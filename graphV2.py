#!/usr/bin/env python
# encoding: utf-8

import codecs
import os
import subprocess
import pymysql
testivr = -1


def chemin(dest):
#	print dest
#	print listeDest
	global testivr
#	print str(testivr)
	mycursor.execute("select category_id from ombu_destinations where destination_id=%s", (dest,))
	category = mycursor.fetchone()[0]
	mycursor.execute("select `index` from ombu_destinations where destination_id=%s", (dest,))
	ind = mycursor.fetchone()[0]
#	print category
#	print ind

	mycursor.execute("select name from ombu_destination_categories where category_id=%s", (category,))
	name = mycursor.fetchone()[0]
#	print name
	
	if name == 'announcement':
		mycursor.execute("select destination_id from ombu_announcements where announcement_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
#		print dest
		mycursor.execute("select description from ombu_announcements where announcement_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "Annonce "
		listeDest.append(nomType + nom)
		if dest not in listeDest :
			listeDest.append(dest)
			with codecs.open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("Annonce : ")
				schema.write(str(nom))
				schema.write("\"")
			if str(testivr) != "-1":
				with codecs.open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=black]")
				schema.write("\"")
				schema.write("Annonce : ")
				schema.write(str(nom))
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write("Annonce : ")
						schema.write(str(nom))
						schema.write("\"")
					if str(testivr) != "-1":
						with open('%s.dot' % did, 'a') as schema:
							schema.write("[label = \"")
							schema.write(str(testivr))
							schema.write("\"]")
						testivr = -1
					with open('%s.dot' % did, 'a') as schema:
						schema.write("edge [color=black]")
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
#                                		schema.write("\" -- \"")
#						schema.write(str(listeDest[x+1]))
						schema.write("\"")
#					print (str(listeDest[x+1]))
#			print ("BOUCLE")
	elif name == 'queue':
		mycursor.execute("select destination_id from ombu_queues where queue_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_queues where queue_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "Queue "
		listeDest.append(nomType + nom)
		if dest not in listeDest :
#			print dest
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("Queue : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select extension_id from ombu_queue_members where queue_id=%s", (ind,))
			cursor = mycursor
#			print ("indice")
#			print ind
			del liste3[:]
			for i in cursor:
				extension = i[0]
				liste3.append(extension)
#				print liste3
			for i in range (len(liste3)):
				mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
				extension = mycursor.fetchone()[0]
#				print extension
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(extension))
					schema.write(" ")
				if (i+1)%5 == 0:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
			if str(testivr) != "-1":
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=black]")
				schema.write("\"")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("Queue : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select extension_id from ombu_queue_members where queue_id=%s", (ind,))
			cursor = mycursor
#                       print ("indice")
#                       print ind
			del liste3[:]
			for i in cursor:
				extension = i[0]
				liste3.append(extension)
#                               print liste3
			for i in range (len(liste3)):
				mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
				extension = mycursor.fetchone()[0]
#                               print extension
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(extension))
					schema.write(" ")
				if (i+1)%5 == 0:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:	
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
						schema.write("\n")
					mycursor.execute("select extension_id from ombu_queue_members where queue_id=%s", (ind,))
					cursor = mycursor
#                      			print ("indice")
#                       		print ind
					del liste3[:]
					for i in cursor:
						extension = i[0]
						liste3.append(extension)
#                               		print liste3
						for i in range (len(liste3)):
							mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
							extension = mycursor.fetchone()[0]
#                               			print extension
							with open('%s.dot' % did, 'a') as schema:
								schema.write(str(extension))
								schema.write(" ")
							if (i+1)%5 == 0:
								with open('%s.dot' % did, 'a') as schema:
									schema.write("\n")
#                                					schema.write("\" -- \"")
#                                					schema.write(listeDest[x+1])
							with open('%s.dot' % did, 'a') as schema:
								schema.write("\"")
						if str(testivr) != "-1":
							with open('%s.dot' % did, 'a') as schema:
								schema.write("[label = \"")
								schema.write(str(testivr))
								schema.write("\"]")
								schema.write("edge [color=black]")
						testivr = -1
					
#                       	print ("BOUCLE")
	elif name == 'extension':
		mycursor.execute("select extension from ombu_extensions where extension_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
			schema.write("\"")
			schema.write("Extension : ")
			schema.write(str(nom))
			schema.write("\"")
		if str(testivr) != "-1":
			with open('%s.dot' % did, 'a') as schema:
				schema.write("[label = \"")
				schema.write(str(testivr))
				schema.write("\"]")
			testivr = -1
			
	elif "voicemail" in name:
		mycursor.execute("select extension from ombu_extensions where extension_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
			schema.write("\"")
			schema.write("Voicemail : ")
			schema.write(str(nom))
			schema.write("\"")
		if str(testivr) != "-1":
			with open('%s.dot' % did, 'a') as schema:
				schema.write("[label = \"")
				schema.write(str(testivr))
				schema.write("\"]")
			testivr = -1

#		print ("Fin")
	elif name == 'ringgroup':
		mycursor.execute("select destination_id from ombu_ring_groups where ring_group_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_ring_groups where ring_group_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "RG "
		listeDest.append(nomType + nom)
		if dest not in listeDest :
#			print dest
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("RG : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select extension_id from ombu_ring_group_members where ring_group_id=%s", (ind,))
			cursor = mycursor
#                        print ("indice")
#                        print ind
			for i in cursor:
				extension = i[0]
				liste3.append(extension)
#                                print liste3
			for i in range (len(liste3)):
				mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
				extension = mycursor.fetchone()[0]
#                                print extension
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(extension))
					schema.write(" ")
				if (i+1)%5 == 0:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
			if str(testivr) != "-1":
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=black]")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("RG : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select extension_id from ombu_ring_group_members where ring_group_id=%s", (ind,))
			cursor = mycursor
#                       print ("indice")
#                       print ind
			del liste3[:]
			for i in cursor:
				extension = i[0]
				liste3.append(extension)
#                                print liste3
			for i in range (len(liste3)):
				mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
				extension = mycursor.fetchone()[0]
#                               print extension
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(extension))
					schema.write(" ")
				if (i+1)%5 == 0:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
#                                		schema.write("\" -- \"")
#                                		schema.write(str(listeDest[x+1]))
					mycursor.execute("select extension_id from ombu_ring_group_members where ring_group_id=%s", (ind,))
					cursor = mycursor
#                       		print ("indice")
#                       		print ind
					for i in cursor:
						extension = i[0]
						liste3.append(extension)
#                               		print liste3
					for i in range (len(liste3)):
						mycursor.execute("select extension from ombu_extensions where extension_id=%s", (liste3[i],))
						extension = mycursor.fetchone()[0]
#                               		print extension
						with open('%s.dot' % did, 'a') as schema:
							schema.write(str(extension))
							schema.write(" ")
						if (i+1)%5 == 0:
							with open('%s.dot' % did, 'a') as schema:
								schema.write("\n")
					with open('%s.dot' % did, 'a') as schema:	
						schema.write("\"")
					if str(testivr) != "-1":
						with open('%s.dot' % did, 'a') as schema:
							schema.write("[label = \"")
							schema.write(str(testivr))
							schema.write("\"]")
						testivr = -1
					with open('%s.dot' % did, 'a') as schema:
						schema.write("edge [color=black]")
#                	print ("BOUCLE")
	elif name == 'trunk':
		mycursor.execute("select description from ombu_trunks where trunk_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
			schema.write("\"")
			schema.write("Trunk : ")
			schema.write(str(dest))
			schema.write("\"")
		if str(testivr) != "-1":
			with open('%s.dot' % did, 'a') as schema:
				schema.write("[label = \"")
				schema.write(str(testivr))
				schema.write("\"]")
			testivr = -1
		with open('%s.dot' % did, 'a') as schema:
			schema.write("edge [color=black]")
			
#                print dest
	elif name == 'disa':
		mycursor.execute("select description from ombu_disa where disa_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("DISA : ")
				schema.write(str(dest))
				schema.write("\"")
		if str(testivr) != "-1":
			with open('%s.dot' % did, 'a') as schema:
				schema.write("[label = \"")
				schema.write(str(testivr))
				schema.write("\"]")
			testivr = -1
		with open('%s.dot' % did, 'a') as schema:
			schema.write("edge [color=black]")
#                print dest
	elif name == 'ivr':
		mycursor.execute("select description from ombu_ivrs where ivr_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "IVR : "
#                print nom
		mycursor.execute("select destination_id from ombu_ivr_entries where ivr_id=%s", (ind,))
		listeIVR = []
		for x in mycursor: 
			dest = x[0]
#                	print dest
			listeIVR.append(dest)
		listeDest.append(nomType + nom)
		if dest not in listeDest :
			listeDest.append(dest)
			for i in range(len(listeIVR)):
				mycursor.execute("select option from ombu_ivr_entries where ivr_id=%s and destination_id=%s", (ind,listeIVR[i],))
				with open('%s.dot' % did, 'a') as schema:
					schema.write("\"")
					schema.write("IVR : ")
					schema.write(str(nom))
					schema.write("\"")
				if str(testivr) != "-1":
					with open('%s.dot' % did, 'a') as schema:
						schema.write("[label = \"")
						schema.write(str(testivr))
						schema.write("\"]")
					testivr = -1
				testivr = mycursor.fetchone()[0]
				with open('%s.dot' % did, 'a') as schema:
					schema.write("edge [color=black]")
					schema.write("\"")
					schema.write("IVR : ")
					schema.write(str(nom))
					schema.write("\" -- ")
				chemin(listeIVR[i])
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write("IVR : ")
						schema.write(str(nom))
						schema.write("\"")
					if str(testivr) != "-1":
						with open('%s.dot' % did, 'a') as schema:
							schema.write("[label = \"")
							schema.write(str(testivr))
							schema.write("\"]")
						testivr = -1
					with open('%s.dot' % did, 'a') as schema:
						schema.write("edge [color=black]")
						schema.write("\"")
						schema.write("IVR ")
						schema.write(": ")
						schema.write(str(nom))
#                                               schema.write("\" -- \"")
#                                               schema.write(str(listeDest[x+1]))
						schema.write("\"")

			
	elif name == 'nightmode':
		mycursor.execute("select enabled_destination_id from ombu_nightmodes where nightmode_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
#                print dest
		mycursor.execute("select description from ombu_nightmodes where nightmode_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "NM "
		listeDest.append(nomType + nom)
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("NM : ")
				schema.write(str(nom))
				schema.write("\"")
			if str(testivr) != "-1":
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("NM : ")
				schema.write(str(nom))
				schema.write("\"")
			mycursor.execute("select state from ombu_nightmodes where nightmode_id=%s", (ind,))
			etat = mycursor.fetchone()[0]
			if etat == "no" :
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[color=red] ")
			else :
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[color=green] ")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=green]")
				schema.write("\"")
				schema.write("NM : ")
				schema.write(str(nom))
				schema.write("\"")
				schema.write(" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
#						schema.write("\" -- \"")
#                                		schema.write(str(listeDest[x+1]))
						schema.write("\"")
					if str(testivr) != "-1":
						with open('%s.dot' % did, 'a') as schema:
							schema.write("[label = \"")
							schema.write(str(testivr))
							schema.write("\"]")
						testivr = -1
				
#                	print ("BOUCLE")
		mycursor.execute("select disabled_destination_id from ombu_nightmodes where nightmode_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
#                print dest
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write(" \"")
				schema.write("NM : ")
				schema.write(str(nom))
				schema.write("\"")
			mycursor.execute("select state from ombu_nightmodes where nightmode_id=%s", (ind,))
			etat = mycursor.fetchone()[0]
			if etat == "no" :
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[color=red] ")
			else :
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[color=green] ")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=red]")
				schema.write(" \"")
				schema.write("NM : ")
				schema.write(str(nom))
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
#                        		        schema.write("\" -- \"")
#                        		        schema.write(str(listeDest[x+1]))
						schema.write("\"")
#                        print ("BOUCLE")
	elif name == 'time_condition':
		listetime = [1]
		mycursor.execute("select match_destination_id from ombu_time_conditions where time_condition_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_time_conditions where time_condition_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		nomType = "TC "
		listeDest.append(str(nomType) + str(nom))
#                print dest
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
				schema.write("TC : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select time_group_id from ombu_time_conditions where time_condition_id=%s", (ind,))
			timegroup = mycursor.fetchone()[0]
			mycursor.execute("select time from ombu_time_groups_schedules where time_group_id=%s", (timegroup,))
			cursor = mycursor
			for i in cursor:
				listetime[0] = i
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(listetime[0]))
					schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
			if str(testivr) != "-1":
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=green]")
				schema.write("\"")
				schema.write("TC : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select time_group_id from ombu_time_conditions where time_condition_id=%s", (ind,))
			timegroup = mycursor.fetchone()[0]
			mycursor.execute("select time from ombu_time_groups_schedules where time_group_id=%s", (timegroup,))
			cursor = mycursor
			for i in cursor:
				listetime[0] = i
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(listetime[0]))
					schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
						schema.write("\n")
					mycursor.execute("select time_group_id from ombu_time_conditions where time_condition_id=%s", (ind,))
					timegroup = mycursor.fetchone()[0]
					mycursor.execute("select time from ombu_time_groups_schedules where time_group_id=%s", (timegroup,))
					cursor = mycursor
					for i in cursor:
						listetime[0] = i
						with open('%s.dot' % did, 'a') as schema:
							schema.write(str(listetime[0]))
							schema.write("\n")
					with open('%s.dot' % did, 'a') as schema:
						schema.write("\"")
					if str(testivr) != "-1":
						with open('%s.dot' % did, 'a') as schema:
							schema.write("[label = \"")
							schema.write(str(testivr))
							schema.write("\"]")
						testivr = -1
#                		        schema.write("\" -- \"")
#                      			schema.write(str(listeDest[x+1]))
#                                	schema.write("\"")
					return

#                        print ("BOUCLE")
		mycursor.execute("select mismatch_destination_id from ombu_time_conditions where time_condition_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
#                print dest
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
				schema.write(" \"")
				schema.write("TC : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select time_group_id from ombu_time_conditions where time_condition_id=%s", (ind,))
			timegroup = mycursor.fetchone()[0]
			mycursor.execute("select time from ombu_time_groups_schedules where time_group_id=%s", (timegroup,))
			cursor = mycursor
			for i in cursor:
				listetime[0] = i
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(listetime[0]))
					schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\"")
			if str(testivr) != "-1":
				with open('%s.dot' % did, 'a') as schema:
					schema.write("[label = \"")
					schema.write(str(testivr))
					schema.write("\"]")
				testivr = -1
			with open('%s.dot' % did, 'a') as schema:
				schema.write("edge [color=red]")
				schema.write("\"")
				schema.write("TC : ")
				schema.write(str(nom))
				schema.write("\n")
			mycursor.execute("select time_group_id from ombu_time_conditions where time_condition_id=%s", (ind,))
			timegroup = mycursor.fetchone()[0]
			mycursor.execute("select time from ombu_time_groups_schedules where time_group_id=%s", (timegroup,))
			cursor = mycursor
			for i in cursor:
				listetime[0] = i
				with open('%s.dot' % did, 'a') as schema:
					schema.write(str(listetime[0]))
					schema.write("\n")
			with open('%s.dot' % did, 'a') as schema:
				schema.write("\" -- ")
			chemin(dest)
		else :
			for x in range(len(listeDest)):
				if listeDest[x] == dest:
					with open('%s.dot' %did, 'a') as schema:
						schema.write("\"")
						schema.write(str(nomType))
						schema.write(": ")
						schema.write(str(nom))
#                		                schema.write("\" -- \"")
#                		                schema.write(str(listeDest[x+1]))
						schema.write("\"")
#					print (str(listeDest[x+1]))
#                        print ("BOUCLE")
	elif name == 'terminate_call':
		with open('%s.dot' % did, 'a') as schema:
			schema.write("\"Terminate : ")
			schema.write(str(did))
			schema.write("\"")
		if str(testivr) != "-1":
			with open('%s.dot' % did, 'a') as schema:
				schema.write("[label = \"")
				schema.write(str(testivr))
				schema.write("\"]")
			testivr = -1
		with open('%s.dot' % did, 'a') as schema:
			schema.write("edge [color=black]")
	elif name == 'custom_destination':
		mycursor.execute("select destination from ombu_custom_destinations where custom_destination_id=%s", (ind,))
		custDest = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
                        schema.write("\"Custom Dest : ")
                        schema.write(str(custDest))
                        schema.write("\"")
		if str(testivr) != "-1":
                        with open('%s.dot' % did, 'a') as schema:
                                schema.write("[label = \"")
                                schema.write(str(testivr))
                                schema.write("\"]")
                        testivr = -1
		with open('%s.dot' % did, 'a') as schema:
			schema.write("edge [color=black]")

#		print("Fin")
#	else:
#		print("Fin")

did = 0000000000
category = 0
ind = 0
dest = 0
dest2 = 0
name = 'abc'
nomType = 'abc'
extension = 0
liste3 = []

mydb = pymysql.connect(
	host="localhost",
	user="root",
	database="ombutel"
)
mycursor = mydb.cursor()

mycursor.execute("select destination_id, did from ombu_inbound_routes")
cursor = mycursor
liste1 = []
#print (liste1)
liste2 = []
#print (liste2)

for i in cursor:
#	print i
	dest = i[0]
#	print dest
#	print type(dest)
#	print type(dest)
	liste1.append(dest)
#	print (liste1)
	dest = i[1]
	liste2.append(dest)
#	print (liste2)

#print liste2[0]

Date = subprocess.check_output("date", shell=True)
os.system("mkdir /usr/share/ombutel/www/graph")

for i in range(len(liste1)):
#	print (liste2[i])
	did = liste2[i]
	listeDest = [liste1[i]]
#	print (listeDest)
	with open('%s.dot' % did, 'w') as schema:
		schema.write("graph schema {")
	with open('%s.dot' % did, 'a') as schema:
		schema.write(" \n ")
		schema.write("node [shape=box]")
		schema.write(" \n \"")
		schema.write(str(Date))
		schema.write(" \n \"")
		schema.write(" \n \"")
		schema.write(str(did))
		schema.write("\" -- ")
	chemin(liste1[i])
#	print (listeDest)
	with open('%s.dot' % did, 'a') as schema:
		schema.write("\n;}\n")
	os.system("dot -Tpdf '{0}'.dot -o '{0}'.pdf".format(did))
	fileName = r"/usr/share/ombutel/www/graph"
#	if os.path.exists(fileName):
#		print("ok")
#	else:
	os.system("mv '{0}'.pdf /usr/share/ombutel/www/graph/'{0}'.pdf ".format(did))
	listeDest = []
	liste3 = []
	testivr = -1
