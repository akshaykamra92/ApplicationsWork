import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()

word = input("Enter the word to be searched ")
query = cursor.execute("Select * from Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('No Word found!')