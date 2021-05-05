import mysql.connector


def databaseConnexion():
    """Fonction permettant de creer une instance de connexion
       [Author] : Mouhammad Sylla @mouha09 

    Returns:
        [databaseInstance]: [Instance de la base de donnée]
    """
    databaseInstance = mysql.connector.connect(
        host = "localhost",
        password = "root",
        username = "root",
        port = "8889",
        database = "janguattcovid"
    )
    
    return databaseInstance

