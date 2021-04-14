#Twint est un module gratuit utilise pour recuperer des tweets gratuitment sans authentification 
import twint


# Configurer le twint 
c = twint.Config()
c.Username="MinisteredelaS1"
c.Output = "ImagesCommunique.csv"
c.Store_csv = True
c.Images=True
#Recuperation des tweets 

twint.run.Search(c)



#Telecharger les images sur le dossier csv 

import csv
liste=[]
with open('ImagesCommunique.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      liste.append(row['thumbnail'])
      
import urllib.request
for i in range(1 ,514):    
     urllib.request.urlretrieve(liste[i] ,"./ImagesCommuniques/communique"+str(i)+".jpg")
     print("Picture Download with Success")



 


 




def cleanText(text):
    """Fonction permettant de nettoyer un peu le texte pour supprimer certaines données superrflux
       Author : Mouhammad Sylla mouha@09  
    Args:
        text ([string]): [Texte à nettoyer]

    Returns:
        [string]: [Retourne le texte apres nettoyage ]
    """
    specialCharacter =  '''!()-[]{};:'"\,<>./?@#$%^&*_~v¥V'''
    
    text = str(text)
    for word in text:
        if word in specialCharacter:
            text = text.replace(word,"") #Suppression des ponctuations et des caracteres speciauxx
            
    
    return text



from PIL import Image 
import pytesseract as pt 
import os  

# telecharger les images des commmuniques  2 3,4
for  i in range(2,4):
     image='./ImagesCommuniques/communiquee'+str(i)+'.jpg'
     text=pt.image_to_string(Image.open(image))
     text=cleanText(text)
     ###  Write to Text File ######
     file = open("./FileText/communique"+str(i),"w")
     file.write(text)
     print(text)



#Telechargement des images des communiques de 5 a 400
for  i in range(4,400):
        image='./ImagesCommuniques/communiquee'+str(i)+'.jpg'
        text=pt.image_to_string(Image.open(image))
        text=cleanText(text)
     ###  Write to Text File ######
        file = open("./FileText/communique"+str(i+1),"w")
        file.write(text)
        print(text)

