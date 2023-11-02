from bs4 import BeautifulSoup
from twilio.rest import Client
import sqlite3


sendMSG = False

# Set up secrets
def get_secret(filename, key, subkey):
    try:
        with open(filename) as f:
            data = json.load(f)
            return data[key][subkey]
    except Exception as e:
        print("Error: ", e)

# Get Twilio secrets from secrets.json
account_sid = get_secret('secrets.json', "twilio", "account_sid")
auth_token = get_secret('secrets.json', "twilio", "auth_token")
fromNumber = get_secret('secrets.json', "twilio", "from_number")
toNumber = get_secret('secrets.json', "twilio", "to_number")

client = Client(account_sid, auth_token)


# Set up database if it doesn't exist already
def db_setUp_scratch():
    conn = get_db_connection()

    with open('initDB.sql') as f:
        conn.executescript(f.read())

        f.close()
    conn.commit()
    conn.close()


# Set up DB connections
def get_db_connection():
    conn = sqlite3.connect('drugTest.db')
    conn.row_factory = sqlite3.Row
    return conn


# Write function to create a new user in the database

# Figure out the best way to pass lists to the databse,
# I'm thinking just passing it a bare string like
# "Black, Blue, Orange" will be the easiest

def addUser(userName, phoneNumber, colors):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (userName, phoneNumber, colors) VALUES (?, ?, ?)",
                (userName, phoneNumber, colors))
    conn.commit()
    conn.close()


# Write a function to fetch a user from the database into a user object

def fetchUserByName(userName):
    conn = get_db_connection()
    cur = conn.cursor()
    record = cur.execute("SELECT * FROM users WHERE userName = ?", userName)
    conn.close()
    return record



# Write code to iterate over the DB
def dbIterate():
    conn = get_db_connection()
    cur = conn.cursor()
# Execute the loop for each user in the DB (Get colors, Compare, Send text)



def sendMessage(fromNumber, toNumber, called):
    if (called):
        message = client.messages.create(
            from_=fromNumber,
            body='Your color was called today. Make sure to go to the testing center today ',
            to=toNumber
        )
        print(message.sid)
    else:
        message = client.messages.create(
            from_=fromNumber,
            body='Your color was not called today ',
            to=toNumber
        )
        print(message.sid)


# Actually, lets just abstract the main logic of the program, then handle the DB operations in the main loop and call this

# Let's just pretend we have the init DB with 2 users then FIO later

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    conn = get_db_connection()

    called = False
    myColors = ["White", "Black"]

# You will need to wget the page of the testing agency you're using

    with open("index.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    line = soup.h4.getText()

    colors = line.split(":")
    colorsList = colors[1]
    print(colorsList.split(","))

    colorListString = repr(colorsList).split(",")
    for color in myColors:
        for x in colorListString:
            x = x.strip(" ")
            x = x.replace("'", "")
            if (x.strip(" ") == color):
                print(x.strip(" ") + " was matched\n")
                called = True
                break
            else:
                print(x.strip(" ") + " was not a match\n")

    if (called):
        sendMessage(fromNumber, toNumber, called)
        print("Your Color was called Today")


    else:
        sendMessage(fromNumber, toNumber, called)
        print("Your Color was not called today")
