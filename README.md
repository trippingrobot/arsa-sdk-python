# Arsa Python SDK

Welcome to the Arsa Python SDK. This sdk will help to create and deploy your api to Arsa. Simply
wrap your route endpoints with Arsa generators and code your application logic. In one command
deploy your api to arsa.io and you're done.

## Quick Start Guide

Install the sdk using pip like so...

```
pip install arsa-sdk
```

Configure your project for Arsa.

```
arsa config
```

Create a `handler.py` file to handle your API routes

```python
import arsa-sdk

@Arsa.get("/users")
def list_users():
    """ Get users """
    return [{'id':'124', 'name':'Bob Star', 'email':'bob@star.io'}]

@Arsa.post("/users")
@Arsa.authenticate
def create_user(name, **kwargs):
    """ Create user if client is authenticated """
    return {'id':'124', 'name':name, 'email':kwargs['email']}

@Arsa.get("/accounts/{account_id}")
def get_account(account_id):
    """ Get account with params """
    return [{'id':account_id, 'name':'Acme Inc.', 'email':'support@acme.io'}]

@Arsa.post("/users")
@Arsa.authenticate
@Arsa.validate(name='string')
def create_account(name, **kwargs):
    """ Create account and make sure 'name' parameter is passed as a string """
    return {'id':'124', 'name':name}
```

Test your API

```
arsa run

curl http://localhost:3000/users
```

Deploy your API to arsa.io

```
arsa deploy
```
