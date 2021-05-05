from  packages.apis.services.database_config import databaseConnexion
from mysql.connector import Error
import hashlib


def checkUser(username, password):
    """Fonction permettant d'authentifier un utilisateur en fonction des identifiants
       Author : Mouhammad Sylla @mouha09

    Args:
        username ([string]): [nom d'utilisateur]
        password ([string]): [mot de passe]

    Returns:
        [tuple]: [retourne le nom et le prenom]
    """
    
    try:
        databaseInstance = databaseConnexion()
    except Error as e:
        return False
    
    #print(databaseInstance)
    
    request = "select prenom,nom from user where username=%s and password=%s"
    params = (username, hashlib.md5(password.encode("utf-8")).hexdigest()) #Encodage en utilisant l'algorithme md5 de hashlib
    cursor = databaseInstance.cursor()
    cursor.execute(request,params)
    
    result = cursor.fetchone()
    cursor.close()

    if result : 
        return result
    else:
        return False


    