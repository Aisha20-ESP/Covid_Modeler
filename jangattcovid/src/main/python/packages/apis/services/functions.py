import pdf2image
from PIL import Image
import pytesseract
import os
import requests


def downloadFile(url):
    """Fonction permettant de telecharger tous les fichiers pdf
       Author: Mouhammad Sylla @mouha09

    Args:
        url ([type]): [description]
    """

    # Recuperation du nom du fichier à travers un slicing
    temporyNameOfFIle = url[40:]
  

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    # passage de l'url du fichier à telecharger et des headers pour eviter un 403 forbidden 😉
    try:
        request = requests.get(url, headers=headers)
        
        if(request.status_code == 200): #La requete s'est bien executée, la ressource a ete bien recupéree
            
            with open('PdfFiles/'+temporyNameOfFIle, 'wb') as file:  # Ouverture d'un fichier en local
            # Ecriture du contenu du fichier dans le fichier ouvert
                file.write(request.content)
            file.close()
            
            transformPDFToText(temporyNameOfFIle)
        else:
            pass
    except:
        pass

   


def transformPDFToText(path):
    """Fonction permettant de convertir un pdf en image avec le module pdf2image et ensuite de transformer les images en un fichier texte avec le module pytesseract et pillow
       Author : Mouhammad Sylla @mouha09

    Args:
        path ([string]): [Chemin du fichier pdf à transformer en texte]

    Returns:
        [string]: [Cette fonction retourne le nom du ficchier texte qui a ete cree pour recuperer les informations]
    """
    temporyNameOfFIle = path[:-3]
    temporyNameOfFIle =  temporyNameOfFIle.replace('_',"")
    temporyNameOfFIle =  temporyNameOfFIle.replace('-',"")
    

    pages = pdf2image.convert_from_path('PdfFiles/'+path, 200) #Concersion du pdf en image

    #Creation du fichier texte en y copiant le contenu des pdf apres leur transformation en image 
    with open('TextFiles/'+temporyNameOfFIle+'txt', 'wt') as file:
        for index, page in enumerate(pages):
            nameOfImage = temporyNameOfFIle+'_'+str(index)+'jpg'
            page.save(nameOfImage, 'JPEG')
            text = pytesseract.image_to_string(Image.open(nameOfImage))
            text = cleanText(text) #Nettoyage du texte
            file.write(text)
            os.remove(nameOfImage) #Suppresion de l'image apres l'ecriture de son contenu dans le fichier texte
            
    file.close()
    #os.remove(path) #Suppression du fichier pdf initial [à decommenter apres les tests]
    
    return temporyNameOfFIle+'txt' #On retourne le nom du fichier cree au cas ou on en aurait besoin 😉

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