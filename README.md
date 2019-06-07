# celery-email
Simple Email App Using Celery


# Install
Clone this branch
```Bash
git clone -b v2-feature/send-email-beat https://github.com/kevcal69/celery-email.git
```

Before doing compose you have to setup Mailgun API KEYS

```Bash
# Example
MAILGUN_API_URL=https://api.mailgun.net/v3/sandboxbacSomethingkeys.mailgun.org/messages
MAILGUN_API_KEY=mailgun-api-key123
```
After setting up the keys run:
```Bash
docker-compose up
```


# Note
You might see celery errors when first running. That's probably the waiting for the web services to finish the migrations.
Upon starting the servicse the next time, it will show no errors.