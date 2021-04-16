from email_scheduler.scheduler_app import EmailScheduler

# Load Config #
config = {}
with open("email.config") as f:
    for line in f:
        key, value = line.split("::")
        config[key] = value

app = EmailScheduler(config)