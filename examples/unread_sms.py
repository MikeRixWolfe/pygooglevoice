from googlevoice import Voice

voice = Voice()
voice.login()

for message in voice.sms().messages:
    #if not message.isRead:
    print(message.id, message.phoneNumber, message.messageText)
    #message.mark(1)
