import time
import mysql.connector

def connectionToDb():

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
    database='wordsfight'
    )

    return db

def clearWeeklyRoundsData():

    # print('weekly checker called')
    DAYS_PERIOD = time.time() + 604800

    while True:
        
        if time.time() > DAYS_PERIOD:
            db = connectionToDb()
            cursor = db.cursor()
            cursor.execute("UPDATE users SET weekly_rounds = '0' WHERE weekly_rounds > '0'")
            db.commit()
            # print('weekly rounds cleared')

            DAYS_PERIOD += 604800



if __name__ == '__main__':
    clearWeeklyRoundsData()