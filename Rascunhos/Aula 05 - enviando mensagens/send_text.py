from twilio.rest import Client

account_sid = "AC2cf59b8d11782a75eaf583ff359ddd1d"
auth_token = "a1eecf31ae24c6bf4e8f876137079635"
client = Client(account_sid, auth_token)

message = client.messages.create(body='Alguem por ai?',
    to ="+5519996986132",
    from_ ="+19793208009")

print message.sid
