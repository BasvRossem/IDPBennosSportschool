import mysql.connector

cnx = mysql.connector.connect(user='root', password='Benno',
                              host='xxx.xxx.xxx.xxx',
                              database='db3242919')
cursor = cnx.cursor(buffered=True)

code = '000000000000000000000000000000000000000000000000'
query = ("SELECT user_id, status, locatie  FROM user, membership_registration WHERE user.code = '{}' and user_id = membership_registration.user_user_id".format(code))
#SELECT user_id, status FROM User, membership_registration WHERE user.code = '4321' and user_id = membership_registration.user_user_id
#INSERT INTO user(firstname, lastname, email, username, password, code) VALUES ('B','van Rossem','Bas.v.rossem@gmail.com','Messorago','Wachtwoord123','0987654321' )
cursor.execute(query)
for (user_id, status, locatie) in cursor:
    id = user_id
    print(id)
    print("{}, {}".format(status, locatie))
    if locatie == 1:
        cursor.close()
        cursor = cnx.cursor(buffered=True)
        print("Van 1 naar 0")
        #Sql code om die 1 naar een 0 om te zetten
        query = ("UPDATE membership_registration SET locatie = 0 WHERE {} = user_user_id".format(id))
        cursor.execute(query)
        cnx.commit()
    elif locatie == 0:
        cursor.close()
        cursor = cnx.cursor(buffered=True)
        print("van 0 naar 1")
        #sql code om die 0 naar een 1 om te zetten
        query = ("UPDATE membership_registration SET locatie = 1 WHERE {} = user_user_id".format(id))
        cursor.execute(query)
        cnx.commit()
#cnx.commit()


cursor.close()
#cnx.close()