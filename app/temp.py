
import requests,json
r = requests.post("https://sms.telnyx.com/send",
		data=json.dumps({
			"from": "+17733022716",
			"to": "+16304926679",
			"body": "Hi Sachin,  Join Me @AICollab!!!! at Call : Surgery1 at 1 pm Sunday 25th September 2017 Cheer"
			}),
		headers={
			"x-profile-secret": "jSqkQ280CinfZkBBMQj3Do9K",
			"content-type": 'application/json'
		})
print(r.text)