# ColinTestNotification
This is a project to help notify people when they need to submit to random drug testing


# Setup

To get started with this project for your own use you will need a twilio account

You will need to create a secrets.json file formatted in the following way

```
{
  "twilio": {
    "account_sid":""
    "auth_token": ""
    "from_number": "",
    "to_number": ""
  }
}
```

where the `from_number` and `to_number` start with "+1"

Running run.sh will download the html file specified in download.sh
Currently this project only supports Nova Testing, but I hope to add 
more support in the future

Finally, you will need to add your colors into `main.py` in the `myColors` variable
