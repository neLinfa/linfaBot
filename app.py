import json
import requests

# reading the json file
data = json.load(open('intents.json'))
print "Reading JSON File"

# static variables
USER_SLUG = 'nelinfa'
BOT_SLUG = 'linfagreetings'
DEVELOPER_TOKEN = '67b47aace3fbedde816c7fa79fafd18c'
ISOCODE = "IT"

# Looping through the json file to add/update content
for el in data["rasa_nlu_data"]["common_examples"]:
    #intentName = el["intent"]
	# get intents
	response = requests.get('https://api.recast.ai/v2/users/'+USER_SLUG+'/bots/'+BOT_SLUG+'/intents/'+el["intent"]+'',
		headers={'Authorization': 'Token '+DEVELOPER_TOKEN+''}
	)
	# check if intent exists
	if response.json()["message"] == 'Resource not found':
		print "Intent not found, creating new one ..."
		# creating new intent
		responseIntent = requests.post('https://api.recast.ai/v2/users/'+USER_SLUG+'/bots/'+BOT_SLUG+'/intents',
			json={'name': el["intent"]},
			 headers={'Authorization': 'Token '+DEVELOPER_TOKEN+''}
		)
		print (el["intent"] + " Intent Created")
		# creating new expression
		responseExpression = requests.post('https://api.recast.ai/v2/users/'+USER_SLUG+'/bots/'+BOT_SLUG+'/intents/'+el["intent"]+'/expressions',
		  json={'source': el["text"], 'language': {'isocode': ISOCODE}},
		  	headers={'Authorization': 'Token 67b47aace3fbedde816c7fa79fafd18c'}
		)
		print" Expression Created"
		# creating new entity
		#for enel in data["rasa_nlu_data"]["common_examples"]["entities"]:
		#	response = requests.post('https://api.recast.ai/entities',
		#	  json={'name': enel["entity"]},
		#	  headers={'Authorization': 'Token DEVELOPER_TOKEN'}
		#	)
		#	print" Entity Created"
	else:
		print(el["intent"] + " Intent found on BOT")
		# creating new expression
		responseExpression = requests.post('https://api.recast.ai/v2/users/'+USER_SLUG+'/bots/'+BOT_SLUG+'/intents/'+el["intent"]+'/expressions',
		  json={'source': el["text"], 'language': {'isocode': ISOCODE}},
		  	headers={'Authorization': 'Token 67b47aace3fbedde816c7fa79fafd18c'}
		)
		print" Expression Created"
		
		
