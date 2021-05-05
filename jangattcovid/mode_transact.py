
from mysql.connector import connect, DatabaseError, InterfaceError
from mysql.connector.connection import MySQLConnection


class Date():
    def __init__(self):
        
        self.date;
        self.date_heure_extraction;
        self.nbre_test;
        self.nbre_nouv_cas;
        self.nbre_cas_contact;
        self.nbre_cas_importes;
        self.nbre_cas_communautaire;
        self.nbre_deces;
        self.nbre_gueris;
        self.nbre_cas_graves;
    
# ---------------------------------------------------------------------------------
def connexion(host: str(), database: str(), login: str(), pwd: str()):
    # connecte puis déconnecte (login,pwd) de la base [database] du serveur [host]
    # lance l'exception DatabaseError si problème
    connexion = None
    try:
        # connexion
        connexion = connect(host=host, user=login, password=pwd, database=database)
        print(
            f"Connexion réussie à la base database={database}, host={host} sous l'identité user={login}, passwd={pwd}")
    finally:
        # on ferme la connexion si elle a été ouverte
        if connexion:
            connexion.close()
            print("Déconnexion réussie\n")
        
    # ---------------------------------------------------------------------------------
def charger_transac(connexion: MySQLConnection,date_list_insert: list,with_transaction: bool = True):
    # si with_transaction=True alors toute erreur annule l'ensemble des ordres SQL(insertion dans ce cas) exécutés auparavant
    # si with_transaction=False alors une erreur n'a aucun impact sur les ordres SQL exécutés auparavant 

    # initialisations    
    curseur = None
    connexion.autocommit = not with_transaction
    erreurs = []
    try:
        # on demande un curseur
        curseur = connexion.cursor()
        # on  exécute les insertion une à une
        for d in date_list_insert:
            command_insert = "Insert INTO details_cas(date,date_heure_extraction,nbre_test,nbre_nouv_cas,nbre_cas_contact,nbre_cas_importes,nbre_cas_communautaires,nbre_deces,nbre_gueris,nbre_cas_graves) VALUES (d.date,d.date_heure_extraction,d.nbre_test,d.nbre_nouv_cas,d.nbre_cas_contact,d.nbre_cas_importes,d.nbre_cas_communautaires,d.nbre_deces,d.nbre_gueris,d.nbre_cas_graves)"
            try:
                curseur.execute(command_insert)
            except (InterfaceError, DatabaseError) as erreur:
                error = erreur
            # y-a-t-il eu une erreur ?
            if error:
                # une erreur de plus
                msg = f" Erreur :({error})"
                erreurs.append(msg)
        
        
    finally:
        # fermeture du curseur s'il a été obtenu
        if curseur:
            curseur.close()

        # on valide / annule la transaction si elle existe
        if with_transaction:
            if erreurs:
                # annulation
                connexion.rollback()
                return erreurs
            else:
                # validation
                connexion.commit()
# ---------------------------------------------------------------------------------
# ---------------------------------------------- main
# identifiants de la connexion
USER = "root"
PASSWD = ""
HOST = "localhost"
DATABASE = "janguattcovid"

# connexion d'un utilisateur existant
try:
    conect = connexion(host=HOST, login=USER, pwd=PASSWD, database=DATABASE)
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(erreur)
d1 = Date("2021-05-04","2021-04-02",100,20,12,3,9,5,2,1)
d2 = Date("2021-05-05","2021-05-08",80,20,12,3,4,6,3,2)
dates = []
dates.append(d1,d2)
charger_transac(connexion=conect,date_list_insert=dates,with_transaction = True)
