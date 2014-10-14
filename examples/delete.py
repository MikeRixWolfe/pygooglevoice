from googlevoice import Voice

voice = Voice()
voice.login()

for i in xrange(50):
    for message in voice.sms().messages:
        #if message.isRead:
        message.delete()
