class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Sending email with message: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS with message: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Sending push notification with message: {message}"

# Usage
email = EmailNotification()
print(email.send("Hello via Email!"))

sms = SMSNotification()
print(sms.send("Hello via SMS!"))

push = PushNotification()
print(push.send("Hello via Push Notification!"))
