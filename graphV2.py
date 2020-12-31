import os
import subprocess
import mysql.connector

def chemin(dest):
	print dest
	mycursor.execute("select category_id from ombu_destinations where destination_id=%s", (dest,))
	category = mycursor.fetchone()[0]
	mycursor.execute("select `index` from ombu_destinations where destination_id=%s", (dest,))
	ind = mycursor.fetchone()[0]
	print category
	print ind

	mycursor.execute("select name from ombu_destination_categories where category_id=%s", (category,))
	name = mycursor.fetchone()[0]
	print name
	
	if name == 'announcement':
		mycursor.execute("select destination_id from ombu_announcements where announcement_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		print dest
		mycursor.execute("select description from ombu_announcements where announcement_id=%s", (ind,))
                nom = mycursor.fetchone()[0]
		nomType = "Annonce "
		listeDest.append(nomType + nom)
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
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
						schema.write(str(nomType))
                                                schema.write(": ")
                                                schema.write(str(nom))
#                                		schema.write("\" -- \"")
#						schema.write(str(listeDest[x+1]))
                                		schema.write("\"")
			print ("BOUCLE")
	elif name == 'queue':
		mycursor.execute("select destination_id from ombu_queues where queue_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_queues where queue_id=%s", (ind,))
                nom = mycursor.fetchone()[0]
		nomType = "Queue "
                listeDest.append(nomType + nom)
		if dest not in listeDest :
			print dest
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("Queue : ")
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
#                                		schema.write("\" -- \"")
#                                		schema.write(listeDest[x+1])
                                		schema.write("\"")
                       	print ("BOUCLE")
	elif name == 'extension':
		mycursor.execute("select extension from ombu_extensions where extension_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("Extension : ")
				schema.write(str(nom))
                                schema.write("\"")
		print ("Fin")
	elif name == 'ringgroup':
		mycursor.execute("select destination_id from ombu_ring_groups where ring_group_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_ring_groups where ring_group_id=%s", (ind,))
                nom = mycursor.fetchone()[0]
		nomType = "RG "
                listeDest.append(nomType + nom)
		if dest not in listeDest :
			print dest
			listeDest.append(dest)
                        with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("RG :")
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
#                                		schema.write("\" -- \"")
#                                		schema.write(str(listeDest[x+1]))
                                		schema.write("\"")
                	print ("BOUCLE")
	elif name == 'trunk':
		mycursor.execute("select description from ombu_trunks where trunk_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("Trunk : ")
				schema.write(str(dest))
                                schema.write("\"")
                print dest
	elif name == 'disa':
		mycursor.execute("select description from ombu_disa where disa_id=%s", (ind,))
                dest = mycursor.fetchone()[0]
		with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("DISA : ")
				schema.write(str(dest))
                                schema.write("\"")
                print dest
	elif name == 'ivr':
		mycursor.execute("select description from ombu_ivrs where ivr_id=%s", (ind,))
		nom = mycursor.fetchone()[0]
                print nom
		mycursor.execute("select destination_id from ombu_ivr_entries where ivr_id=%s", (ind,))
		listeIVR = []
		for x in mycursor: 
			dest = x[0]
                	print dest
			listeIVR.append(dest)
		for i in range(len(listeIVR)):
			with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("IVR : ")
				schema.write(str(nom))
                                schema.write("\" -- ")
        		chemin(listeIVR[i])
	elif name == 'nightmode':
		mycursor.execute("select enabled_destination_id from ombu_nightmodes where nightmode_id=%s", (ind,))
		dest = mycursor.fetchone()[0]
                print dest
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
#						schema.write("\" -- \"")
#                                		schema.write(str(listeDest[x+1]))
                                		schema.write("\"")
                	print ("BOUCLE")
		mycursor.execute("select disabled_destination_id from ombu_nightmodes where nightmode_id=%s", (ind,))
                dest = mycursor.fetchone()[0]
                print dest
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
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
                        print ("BOUCLE")
	elif name == 'time_condition':
		mycursor.execute("select match_destination_id from ombu_time_conditions where time_condition_id=%s", (ind,))
                dest = mycursor.fetchone()[0]
		mycursor.execute("select description from ombu_time_conditions where time_condition_id=%s", (ind,))
                nom = mycursor.fetchone()[0]
		nomType = "TC "
                listeDest.append(str(nomType) + str(nom))
                print dest
		if dest not in listeDest :
			listeDest.append(dest)
			with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"")
				schema.write("TC : ")
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
#                		                schema.write("\" -- \"")
#                      			        schema.write(str(listeDest[x+1]))
                                		schema.write("\"")
                        print ("BOUCLE")
		mycursor.execute("select mismatch_destination_id from ombu_time_conditions where time_condition_id=%s", (ind,))
                dest = mycursor.fetchone()[0]
                print dest
		if dest not in listeDest :
			listeDest.append(dest)
                        with open('%s.dot' % did, 'a') as schema:
                                schema.write(" \"")
				schema.write("TC : ")
				schema.write(str(nom))
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
                        print ("BOUCLE")
	elif name == 'terminate_call':
		with open('%s.dot' % did, 'a') as schema:
                                schema.write("\"Terminate : ")
				schema.write(str(did))
				schema.write("\"")
		print("Fin")
	else:
		print("Fin")

did = 0000000000
category = 0
ind = 0
dest = 0
dest2 = 0
name = 'abc'
nomType = 'abc'

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	database="ombutel"
)
mycursor = mydb.cursor()

mycursor.execute("select destination_id, did from ombu_inbound_routes")
cursor = mycursor
liste1 = []
print (liste1)
liste2 = []
print (liste2)

for i in cursor:
	print i
	dest = i[0]
	print dest
	print type(dest)
	print type(dest)
	liste1.append(dest)
	print (liste1)
	dest = i[1]
	liste2.append(dest)
	print (liste2)

print liste2[0]



for i in range(len(liste1)):
	print (liste2[i])
	did = liste2[i]
	listeDest = [liste1[i]]
	print (listeDest)
	with open('%s.dot' % did, 'w') as schema:
		schema.write("graph schema {")
	with open('%s.dot' % did, 'a') as schema:
	        schema.write(" \n \"")
		schema.write(str(did))
		schema.write("\" -- ")
	chemin(liste1[i])
	print (listeDest)
	with open('%s.dot' % did, 'a') as schema:
                schema.write("\n;}\n")
	listeDest = []
