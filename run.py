from email_scheduler import app

if __name__ == "__main__":
    app.add_email_event("garage_inquiry.txt")
    app.run()