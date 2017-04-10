#!/usr/bin/python

#
# http://mattharris.org/2015/06/23/trello-api-basics/
#

import requests
import json

'''
Basic GET request to trello API to pull basic board details
'''
app_key  = '341b3e8f74d4234c57c6c29dccd3859c'
token    = '1df6939f87352919288f7ba387811ac76c0e52892466ed835779ff09468d486d'
# Board: RPA, Test automation
board_id = '58bd0fc9ba13b0dd6906154c'

# Get board data with board ID
url      = 'https://api.trello.com/1/board/' + board_id + '?key=' + app_key + '&token=' + token
r        = requests.get(url)
print(json.dumps(r.text))

# Get all boards
url      = 'https://api.trello.com/1/board/' + board_id + '/cards/?key=' + app_key + '&token=' + token
r        = requests.get(url)
print(json.dumps(r.text))

# Get lists
url     = 'https://api.trello.com/1/board/' + board_id + '/lists/?key=' + app_key + '&token=' + token
r        = requests.get(url)
print(json.dumps(r.text))

# Get cards on lists
print('Get Cards on list\n')
url     = 'https://api.trello.com/1/boards/' + board_id + '/lists?cards=open&card_fields=name&fields=name&key=' + app_key + '&token=' + token
r        = requests.get(url)
print(json.dumps(r.text))

# create card
print('Create card\n')
destinationList = '58bd40dc78c9fc2fc3e6522c'
newCard = {'name': 'I just created a second new card!', 
           'desc': 'Using the Trello API is fun and easy!',
           'pos': 'top', 
           'idList': destinationList
          }

url     = 'https://api.trello.com/1/cards/?key=' + app_key + '&token=' + token
r        = requests.post(url, newCard)
print(json.dumps(r.text))
