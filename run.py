from email_scheduler import app

if __name__ == "__main__":
    # app.send_email(['erhanthorn@gmail.com'], 'This is a test', 'This is the body of a test email')
    app.add_email_event(['erhanthorn@gmail.com'], 'This is a test', 'This is the body of a test email')
    app.run()