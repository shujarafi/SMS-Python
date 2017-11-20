import gammu
import sqlite3


def funcSMS(insname, insphone):
    Phnumber = insphone
    NameSMS = insname

    sm = gammu.StateMachine()
    sm.ReadConfig()
    sm.Init()

    message = {
        'Text': 'The great idiot ' + NameSMS,
        'SMSC': {'Location': 1},
        'Number': Phnumber,
    }

    sm.SendSMS(message)

#Idffp = 0 #ID from fingerprint scanner


def getfromDB(inIDFFP):
    ### DB Related
    db = sqlite3.connect("numbDB.db")
    cursor = db.cursor()


    cursor.execute("""SELECT ID, Name, Number FROM Numbers""")
    user = cursor.fetchall() ## Fetching all from DB

    MYIDFFP = inIDFFP

    FromFetched = (user[MYIDFFP])
    PhnumDB = (FromFetched[2]) ##getting phone number from db  ## Understand
    NameDB = FromFetched[1]
    ####

    print("Sending.......")
    funcSMS(NameDB, PhnumDB)
    print("SMS Sent...")

while True:
    Idffp = int(input("In the num"))
    getfromDB(Idffp)
