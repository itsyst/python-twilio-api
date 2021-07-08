from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
call = client.messages.create(
    to=config.twilio_receiver,
    from_=config.twilio_number,
    body="This is a test message"
)
