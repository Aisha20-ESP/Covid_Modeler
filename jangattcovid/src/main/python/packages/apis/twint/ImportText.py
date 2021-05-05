import os 
import json

def search_(entree):
    liste_=["DakarCentre","Mboro","Point-E","CiteApecsy","Sedhiou","CiteDjilyMbaye","GrandDakar","Ngor","CiteSococim","Dieuppeul","DakarOuest","Almadies","DakarPlateau","Wakhinane","CiteFadia","Bambilor","CiteBaobab","Castors","SicapMbao","Derkle","Colobane","Gibraltar","CiteKeurGorgui","CiteTako","Arafat","CiteGadaye","DakarSud","DakarNord","Thies","Kaolack","Guediawaye","HLM","NordFoire","FassMbao","NiaryTaly","CiteSoprim","HLMFass","ZoneDeCaptage","HLMGrandMedine","Mamelles","HLMGrandYoff","Yoff","Ngaparou","Niakou-Rap","Somone","Sacre-Coeur3","Mboro","Sacre-Coeur-3","Sacre-Coeur1","Sacre-Coeur2","Mermoz","KeurMbayeFall","Sebikotane","Touba","Rufisque","Mbour","Mbao","Saint-Louis","Tivaouane","GueuleTapee","Maristes","KeurMassar","Popenguine","Pikine","Ziguinchor","Camberene","Tassette","KeurNdiayeLo","CiteMixta","Malika","BeneBarack","ZakMbao","LacRose","Yarakh","ThiaroyeSurMer","Diamniadio","OuestFoire","Louga","Kedougou","Liberte2","Liberte1","Liberte4","Richard-Toll","Kolda","SicapBaobabs","Sangalkam","Matam","FannResidence","Sokone","Liberte6","Diourbel","Fatick","Yeumbeul","Tambacounda","Velingara","Khombole","Rebeuss","Poute","Dahra","Sedhiou","Bignona","Saraya","Linguere","Kebemer","Mekhe","Kaffrine","NioroduRip","Guinguineo","ThienabaSeck","Joal","Thiadiaye","Mbacke","Podor","Goudiry","Dioffior","Coki","DarouMousty","Sakal","Bambey","Ndoffane","Passy","Saly","Dagana","Kanel","Foundiougne","Salemata","Bounkiling","Pete","Oussouye","Birkilane","Bakel","Thilogne","Koumpentoum","Koungheul","Makacoulibantang","KeurMomarSarr","Thionck-Essyl","Diouloulou","Niakhar","Liberte3","Ouakam","Medina","MedinaYoroFoula","Ranerou","Gossas","MalemHoddar","Diakhao","Kidira","DiankeMakha","Ndiassane","Goudomp","TaibaNdiaye"]
    sortie=""
    count=0
    temp=[]

    for i in range(len(liste_)):
        liste_[i]=liste_[i].lower()
        for i in range(len(liste_)):
            if(entree==""):
                sortie=entree
            if(isinstance(entree,int)):
                sortie=entree
            else:
                if(entree in liste_[i]):
                    sortie=liste_[i]
    return sortie



#--------------------------Fontion pour trouver les anagrammes --------------
def permuter(items):
    if len(items) <= 1:
        return [items]
    liste=[]
    for p in permuter(items[1:]):
        for i in range(len(items)):
            liste.append(p[:i]+items[0:1]+p[i:])
    return liste


def date_(myfile):
   
    maListe = []
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            cdc=myline[1]
            maListe = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc(la ligne 1) dans la liste maListe 

    file.close()
    
    return maListe




def NbreTest_NvCas(myfile):
    maListe = []
    with open("FileText/"+myfile,'r') as file:
        myline = file.readlines()
        length=len(myline)
        for i in range(len(myline)):
            cdc=myline[i]
            if("tests" in cdc ):# On voit si "tests" est présent dans la ligne parcourue
                temp=i #On garde le numéro de la ligne
                maListe = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
            else:
                    pass     
        file.close()
  
    return maListe

def Taux_Positivite(myfile):
    Liste = []
    temp=0
            
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("tests" in cdc ):
                    if("taux de positiité" in cdc):
                        cdc=myline[temp+1]
                        Liste = cdc.split(" ") 
                    else:
                        temp=i
                        cdc=myline[temp+1]
                        Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
    file.close()
    
    return Liste   

def Nbre_Cas_Contact(myfile):
    Liste = []
   
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("Cas contacts" in cdc ):
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
    file.close()
    
    return Liste
def Nbre_Cas_Communautaire(myfile):
    Liste = []
   
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("cas issus de la transmission communautaire" in cdc ):
                    Liste = []
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
    file.close()
    
    return Liste    
def Nbre_Cas_Gueris(myfile):
    Liste = []
   
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("A ce jour" in cdc ):
                    Liste = []
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
    file.close()
    
    return Liste 

#------------Récupération du nombre de décès--------------
def NbreDeces(myfile):
    maListe=[]
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            for i in range(len(myline)):
                cdc=myline[i]
                if("décédés" in cdc ):
                    maListe = []
                    maListe = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                else:
                    pass  
    file.close()
    return maListe    

#--------------------------Récupération des données pour Dakar (Localités et nombre de cas--------------
def Dakar_(myfile):
    Liste = []
    sortie=[]
    fin=0
    debut=0
     #Crétion de liste
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines() #On parcours tout le fichier 
            length=len(myline)#Taille du fichier
            #print(length)
            if(length>=30): #30 est la taille minimale pour pouvoir prendre nos données
                for i in range(len(myline)):
                    cdc=myline[i]
                    if("comme suit" in cdc ):
                        debut=i+2 #Valeur de début pour notre recherche (2 lignes après avoir vu "comme suit")
                for j in range(len(myline)):
                    cdc=myline[j]
                    if("Régions" in cdc):
                        fin=j#Valeur de fin pour notre recherche (après avoir vu "Régions")

                for j in range(debut,fin,1):
                    cdc=myline[j]
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                    #---------Autre nettoyage des valeurs à stocker dans la liste et suppression des valeurs indésirables---------
                    for i in range(len(Liste)-1):
                        Liste[i]= Liste[i].strip(',')
                        b="O,0"
                        for char in b:
                            Liste[i]= Liste[i].replace(char,"")
                        Liste[i].strip('et')
                        if(Liste[i]=="aux"  or Liste[i]==";" or Liste[i]=="-" ):
                            Liste[i]=" "
                        if(Liste[i]=="a"  or Liste[i]=="et" or Liste[i]=="la" or Liste[i]=="au"):
                            Liste[i]=" "
                    Liste = [i for i in Liste if not i.isspace()] #Suppression des espaces dans la liste
                    
                    for i in range(len(Liste)-1):
                        if(Liste[i].isnumeric()):
                            if( Liste[i-1].isnumeric() and isinstance(Liste[i+1], str)  ):
                                Liste[i]=""
                        if(Liste[i].isnumeric()):
                            if( Liste[i-1].isnumeric() and isinstance(Liste[i+1], str)  ):
                                Liste[i]=""

                    for j in range(len(Liste)):
                        specialCharacter =  '''!()[]{};:'"\<>./?@#$%^&*_~v¥V'''
                    if(Liste[j].isnumeric()==False):
                        for char in specialCharacter:
                            Liste[j]= Liste[j].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]
                    #--------------------------------------------------------------------

                    for i in range(len(Liste)-1):
                            if(Liste[i].isnumeric()):
                                Liste[i]=int(Liste[i])#Convertir les valeurs numériques en entier
                    sortie=sortie+Liste
            else:
               print("Le fichier est incomplet, nous ne pouvons pas extraire tous les données que nous avons besoin")#Si la taille du fichier est inférieur à la taille minimale pour extraire nos données
    file.close()
    
    return sortie
    # REgions
def Regions(myfile):
    Liste = []
    sortie= []
    pos=[]
    region=[]
    
        #Crétion de liste
        #*******Pour bien comprendre, veuillez voir la fonction précédente
    fin=0
    debut=0
    with open('FileText/'+myfile,'r') as file:
            myline = file.readlines()
            length=len(myline)
            if(length>=30):
                for i in range(len(myline)):
                    cdc=myline[i]
                    if("Régions" in cdc ):
                        debut=i+1
                for j in range(len(myline)):
                    cdc=myline[j]
                    if("patients suiis" in cdc):
                        fin=j

                for j in range(debut,fin,1):
                    cdc=myline[j]
                    Liste = cdc.split(" ") # la fonction split sépare et enregistre chaque mot de notre cdc dans la liste maListe 
                    for i in range(len(Liste)-1):
                        b="O"
                        for char in b:
                            temp= Liste[i].replace(char,"0")
                            Liste[i]=temp
                        if(Liste[i]=="aux" or Liste[i]=="et" or Liste[i]=="e" or Liste[i]=="," or Liste[i]=="a" or Liste[i]=="-"):
                            Liste[i]=" "
                        if((Liste[i].isnumeric() and Liste[i+1].isnumeric()) ):
                            Liste[i+1]=" "
                        a=","
                        for char in a:
                            Liste[i]= Liste[i].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]

                    for i in range(len(Liste)-1):
                        if(isinstance(Liste[i], int)):
                            if( Liste[i-1]!="-" and isinstance(Liste[i-1], str) and isinstance(Liste[i+1], str)==False  ):
                                Liste[i]=""
                    for j in range(len(Liste)):
                        specialCharacter =  '''!()[]{};:'"\<>./?@#$%^&*_~v¥V'''
                        if(Liste[j].isnumeric()==False):
                            for char in specialCharacter:
                                Liste[j]= Liste[j].replace(char,"")
                    Liste = [i for i in Liste if not i.isspace()]
                    for i in range(len(Liste)-1):
                        if(Liste[i].isnumeric()):
                            Liste[i]=int(Liste[i])
                        else:
                            Liste[i]=str(Liste[i])
                    sortie=sortie+Liste
            else:
                print("Le fichier est incomplet, nous ne pouvons pas extraire tous les données que nous avons besoin")
    file.close()
    
    return sortie

temp=0
length=0
for k in range(401,402):
    mon_fichier=open("FileText/communique"+str(k),"r")
    myline = mon_fichier.readlines() #Parcours du fichier ligne par ligne
    length=len(myline)
    for i in range(len(myline)):
                line=myline[i] #Parcours de ligne mot par mot
                if("COMMUNIQUE" in line ):#Voir si COMMUNIQUE est présent au niveau de la ligne, pour après les lignes précédents
                    temp=i
                else:
                    pass
    liste=[] #Création d'une liste
    for j in range(temp,length,1):#Parcours du texte à partir de la ligne contenant COMMUNIQUE 
        element=myline[j] #On stocke chaque mot de la ligne dans element
        liste.append(element)#On ajoute l'élèment à la liste

    with open('FileText/communique'+str(k),'w') as file:#Ouverture du ficier en mode écriture
            for o in range(len(liste)):#Parcours de la liste créée
                file.write(liste[o])#Ajout des élèments de la liste dans le fichier ouvert
    file.close()

    mon_fichier="communique"+str(k)


    #date__ 
    date__=""
    mois_l=""
    r=[]
    Data=date_(mon_fichier)
    if(len(Data)>4): 
        if(Data[3].isnumeric()):
            Data[2]=Data[3]
            Data[3]=Data[4]
            Data[4]=Data[5]
        lesMois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet','aout','septembre','octobre','novembre','décembre']
        a=","
        for char in a:
            Da= Data[4].split(",")
        for i in range(len(lesMois)-1):
            r=permuter(lesMois[i])#On cherche les anagrammes de la chaine
            for j in range(len(r)):#Si le mois (le mois n'est pas bien écrit), on cherhe s'il est dans un des anagrammes
                if(Data[3] in r[j]):
                    date__=Data[2]+'-'+str(i+1)+'-'+Da[0]
                    mois_l=lesMois[i]
    else:#Dans le cas où le fichier est incomplet
        Annee="null"
        mois_l="null"
        date__="null"
    print (date__)
    print(mois_l)




    #NbTest, Nb nouveaux Cas
    Data0=NbreTest_NvCas(mon_fichier)
    if(len(Data0)<5):#Dans le cas où le fichier est incomplet
        Nbre_Test="null"
        Nbre_Nouveau_Cas="null"
    else:
        Nbre_Test=int(Data0[1])
        Nbre_Nouveau_Cas=int(Data0[4])

    # print (Nbre_Test)    
    print(Nbre_Nouveau_Cas)
    print(Nbre_Test)
    

    #TauxPositivité
    Data1=Taux_Positivite(mon_fichier)
    Taux_Pos=""
    if(len(Data1)<3):#Dans le cas où le fichier est incomplet
        Taux_Pos=0000
    else:
        if(len(Data1)<10):
            for i in range(len(Data1)):
                a=","
                Taux_temp=""
                for char in a:
                    Data1[i]= Data1[i].replace(char,"")
            for i in range(len(Data1)):
                Taux_Pos=Data1[i]
                for j in range(len(Taux_Pos)):
                    if(Taux_Pos[j].isnumeric()):
                        Taux_temp=Taux_temp+Taux_Pos[j]
                    else:
                        pass
                str(Taux_temp)
            Taux_Pos=Taux_temp[0]+"."+Taux_temp[1:3]
            Taux_Pos=float(Taux_Pos)
        else:
            for i in range(len(Data1)):
                a=","
                Taux_temp=""
                for char in a:
                    Data1[i]= Data1[i].replace(char,"")
            for i in range(len(Data1)):
                Taux_Pos=Data1[i]
                for j in range(len(Taux_Pos)):
                    if(Taux_Pos[j].isnumeric()):
                        Taux_temp=Taux_temp+Taux_Pos[j]
                    else:
                        pass
                str(Taux_temp)
            Taux_Pos=Taux_temp[0]+"."+Taux_temp[1:3]
            Taux_Pos=float(Taux_Pos)
        print(Taux_Pos)
       
        #CasContact
    Data2=Nbre_Cas_Contact(mon_fichier)
    if(len(Data2)<2):#Dans le cas où le fichier est incomplet
        Nbre_CasContacts=0000
    else:
        if(isinstance(Data2[0], int)):
            Nbre_CasContacts=Data2[0]
        else:
            Nbre_CasContacts=Data2[1]

    print(Nbre_CasContacts)       

    #CasCommunautaire
    Data3=Nbre_Cas_Communautaire(mon_fichier)
    if(len(Data3)<2):#Dans le cas où le fichier est incomplet
        Nbre_CasCommunautaires=0000
    else:
        if(isinstance(Data3[0], int)):
            Nbre_CasCommunautaires=Data3[0]
        elif(isinstance(Data3[1], int)):
            Nbre_CasCommunautaires=Data3[1]
        else:
            Nbre_CasCommunautaires=Data3[0] 
    print(Nbre_CasCommunautaires)
     
    #NbGuéris
    Data4=Nbre_Cas_Gueris(mon_fichier)
    if(len(Data4)<11):#Dans le cas où le fichier est incomplet
        Nbre_Gueris=0000
    else:
        Nbre_Gueris=int(Data4[10])

    print(Nbre_Gueris)    

    #NbDécès
    Data5=NbreDeces(mon_fichier)
    if(len(Data4)<2):#Dans le cas où le fichier est incomplet
        Nbre_Deces=0000
    else:
        Nbre_Deces=int(Data5[1])
    print(Nbre_Deces)    

    #LesLocalités
    Dakar=Dakar_(mon_fichier) #Récupération de la liste des localités de Dakar
    Dakar=list(filter(None, Dakar)) #Suppression des lignes vides
    region=Regions(mon_fichier)#Récupération de la liste des régions
    region=list(filter(None, region))
    reg= [] #Création de notre liste finale (On y stocke nos données corrigées)
    reg_dkr= []
    if(len(Dakar)!=0 and len(region)!=0):
                    #Correction Ecriture des régions
        for i in range(len(region)):
            if(isinstance(region[i],int)==False):
                region[i]=region[i].replace("\n","")#Suppression des sauts de ligne
                region[i]=region[i].lower()#Mettre les élèments de la liste en miniscule
                a="é,è"
                for word in a :
                    region[i]=region[i].replace(word,"e")#Suppression des accents
            region[i]=search_(region[i])#Correction des erreurs  (niveau ecriture)
        number=0
        for i in range(len(region)):
            if(region[i]==" "):
                region[i]=region[i+1]#Suppression des lignes vides en dupliquant les lignes d'avant
        
        for i in range(len(region)):
            if(isinstance(region[i],int)):
                if(isinstance(region[i+1],str)):
                    number=region[i] #Nombre de cas
                else:
                    pass 
            else:
                reg.append([region[i],number]) #Stockage des régions avec leur nombre de cas
                    #Correction Ecriture des régions
        for i in range(len(Dakar)):
            if(isinstance(Dakar[i],int)==False):
                Dakar[i]=Dakar[i].replace("\n","")
                Dakar[i]=Dakar[i].lower()
                a="é,è"
                for word in a :
                    Dakar[i]=Dakar[i].replace(word,"e")
            Dakar[i]=search_(Dakar[i])
        number=0
        for i in range(len(Dakar)-1):
            if(Dakar[i]==" "):
                Dakar[i]=Dakar[i+1]
       
        for i in range(len(Dakar)-1):
            if(isinstance(Dakar[i],int)):
                if(isinstance(Dakar[i+1],str)):
                    number=Dakar[i]
                else:
                    pass 
            else:
                reg_dkr.append([Dakar[i],number])
    # print(reg_dkr)            
     #Enregistrement des données
    with open('FileTextData/data_donnees'+mon_fichier+'txt','w') as file:
            file.write("id_com %s\n" %mon_fichier)
            file.write("date__ %s\n" %date__)
            file.write("nb_test %s\n" %str(Nbre_Test))
            file.write("nb_nv_cas %s\n" %str(Nbre_Nouveau_Cas))
            file.write("nb_cas_contact %s\n" %str(Nbre_CasContacts))
            file.write("nb_cas_communautaire %s\n" %str(Nbre_CasCommunautaires))
            file.write("nb_gueris %s\n" %str(Nbre_Gueris))
            file.write("nb_deces %s\n" %str(Nbre_Deces))

    file.close()
    # Enregistrement Donnees
    with open('FileTextData/data'+mon_fichier+'txt','a') as file:
            for i in range(0,len(reg)):
                temp=reg[i]
                for j in range(0,len(temp)-1):
                    entree=temp[j].upper()+" "+str(temp[j+1])
                    file.write("%s\n" %entree)
    file.close()
              #Enregistrement des localités de Dakar
    with open('FileTextData/data_dkr'+mon_fichier+'txt','a') as file:
        for i in range(0,len(reg_dkr)):
                temp=reg_dkr[i]
                for j in range(0,len(temp)-1):
                    entree=temp[j].upper()+" "+str(temp[j+1])
                    if(len(entree)>6):
                        file.write("%s\n" %entree)
    file.close()

               #----------------------Les données--------------------------------
    if(os.path.exists("JSONFiles/"+mois_l.upper()+".json")):
            filename_js = 'JSONFiles/'+mois_l.upper()+'.json'
            filename = 'FileTextData/data_donnees'+mon_fichier+'txt'
            # creation of dictionaries
            dict1 = {}
            dict3= {}
            dict2= {}
            Liste_donnees=[]
            fields =['id_com', 'date','nb_test','nb_nv_cas','nb_cas_contact','nb_cas_communautaire','nb_gueris','nb_deces','date_heure_extraction']
            if(os.path.getsize(filename_js)==0):#Si fichier json vide
                with open(filename) as fh:
                    myline = fh.readlines() #On parcours tout le fichier 
                    length=len(myline)#Taille du fichier
                    i=0
                    for line in myline:
                            # reading line by line from the text file
                        description = list( line.strip().split(None, 2))
                        description_=' '.join(description)
                        if(length>1):
                                Liste_donnees.append(description_.split(" ")[1])
                    while i<len(Liste_donnees):
                        dict2[fields[i]]= Liste_donnees[i]
                        i = i + 1
                    dict3[date__]=dict2
                    fh.close()
                    # creating json file        
                out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")# file open in adding mode
                json.dump(dict3, out_file, indent = 4) # Adding 
                out_file.close()
            else:
                with open(filename_js) as foo:
                    data=json.load(foo)
                    with open(filename) as fh:
                        myline = fh.readlines() #On parcours tout le fichier 
                        length=len(myline)#Taille du fichier
                        i=0
                        for line in myline:
                                # reading line by line from the text file
                            description = list( line.strip().split(None, 2))
                            description_=' '.join(description)
                            if(length>1):
                                    Liste_donnees.append(description_.split(" ")[1])
                        while i<len(Liste_donnees):
                            dict2[fields[i]]= Liste_donnees[i]
                            i = i + 1
                        dict3[date__]=dict2
                        data.update(dict3)
                        fh.close()
                    foo.close()
                    # creating json file        
                out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")# file open in adding mode
                json.dump(data, out_file, indent = 4) # Adding 
                out_file.close()


    if(os.path.exists("JSONFiles/"+mois_l.upper()+"_temp.json")):
            filename = 'JSONFiles/'+mois_l.upper()+'_temp.json'
            filename_ = 'FileTextData/data'+mon_fichier+'txt'
            # creation of dictionnariesresultant dictionary
            dict1 = {}
            dict2= {}
            # fields in the sample file 
            with open(filename) as fh:
                data=json.load(fh)
                with open(filename_) as f:
                    for line in f:
                        description = list( line.strip().split(None, 2)) 
                        # loop variable
                        i = 0
                        dict2 = {}
                        while i<len(description):
                            sno =description[0]
                            if(len(description)>1):
                                dict2['NbreCas']= description[i][0]
                            i = i + 1
                        dict1[sno]=dict2
                    data[date__].update(dict1) #Adding the dictionary to the json file
                f.close() 
            out_file = open('JSONFiles/'+mois_l.upper()+'_temp.json', "w")
            json.dump(data, out_file, indent = 3)  
            out_file.close()            
    if(os.path.exists("JSONFiles/"+mois_l.upper()+"_temp.json")):
            filename = 'JSONFiles/'+mois_l.upper()+'_temp.json'
            filename_ = 'FileTextData/data_dkr'+mon_fichier+'txt'
            # creation of dictionnariesresultant dictionary
            dict1 = {}
            dict3= {}
            # fields in the sample file 
            fields =['NomLocalite', 'NbreCas']
        
            with open(filename) as fh:
                data=json.load(fh)
                with open(filename_) as f:
                    for line in f:
                        # reading line by line from the text file
                        description = list( line.strip().split(None, 2)) 
                        # loop variable
                        i = 0
                        dict2 = {}
                        while i<len(description):
                            sno =description[0]
                            if(len(description)>1):
                                dict2['NbreCas']= description[i][0]
                            i = i + 1
                        dict1[sno]= dict2
                    dict3["DAKAR"]=dict1
                    data[date__].update(dict3) #Adding the dictionary to the json file
                f.close() 
            out_file = open('JSONFiles/'+mois_l.upper()+'.json', "w")
            json.dump(data, out_file, indent = 3)  
            out_file.close()
            print(     ">"+mon_fichier+"txt converted to "+mon_fichier+"json")
            os.system("rm JSONFiles/"+mois_l.upper()+"_temp.json")
            print("*****************************************************************************")
    else:
        pass            