import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# get credentials and options
cred = credentials.Certificate('firebase-sdk.json')
params = {
	'databaseURL': 'https://test-app-e0c0d.firebaseio.com/'
}
# init app
firebase_admin.initialize_app(cred, params)

# set data
ref = db.reference('/')
ref.set({
	'Employee': {
		'0': {
			'name': {
				'first': 'sherlock',
				'last': 'holmes'
			},
			'age': 37
		}
	}
})

# update data
ref = db.reference('Employee').child('0').child('name')
ref.set({
	'first': 'Sherlock',
	'middle-initial': 'T',
	'last': 'Holmes'
})


# multiple updates
ref = db.reference('Employee')
ref.update({
	'0/age': 40,
	'0/name/first': 'Sherry'
})

# adding values
ref = db.reference('Employee')
ref.push({
	'name': {
		'first': 'Mario',
	},
	'age': 39
})

# get values
ref = db.reference('Employee')
print(ref.get())
