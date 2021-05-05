import cv2 
import json
import pytesseract
from collections import OrderedDict
img1=cv2.imread("/home/astou/Bureau/Data_Extrac/FileText/communique400")
text1=pytesseract.image_to_string(img1,lang="eng")
print(text1)
month={"JANVIER":1,"FEVRIER":2,"MARS":3,"AVRIL":4,"MAI":5,"JUIN":6,"JUILLET":7,"AOUT":8,"SEPTEMBRE":9,"OCTOBRE":10,"NOVEMBRE":11,"DECEMBRE":12}
class DataExtraction():
    def __init__(self):
        self.num_communique=0,
        self.Date_communique,
        self.Date_extraction,
        self.nbre_tests,
        self.nbre_nouv_cas,
        self.nbre_cas_contacts,
        self.nbre_cas_importes,
        self.nbre_cas_communautaire,
        self.nbre_deces,
        self.nbre_gueris,
        self.nbre_cas_grav,
        self.nbre_vaccines,
        self.nbre_cas_communautaire_par_region,
        self.nbre_cas_communautaire_par_localite_Dakar
        
    def get_num_communique(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="COMMUNIQUE":
                self.num_communique=int(tab_texte[i+1])
                return self.num_communique
    def get_Date_communique(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="Ce":
                #La Date vient apres le "Ce" car le format est Ce ... 
                return tab_texte[i+1]
    def get_nbre_tests(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="tests" or tab_texte[i]=="test":
                #La nbre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="realisés" or tab_texte[i+1]=="realisé":  
                     if (tab_texte[i-1].lower()=="aucun"):
                            tab_texte[i-1]="0"
                     return int(tab_texte[i-1])
                   
    def get_nbre_nouv_cas(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i]=="sont" or tab_texte[i]=="est":
                #La nbre vient apre le premier mot "Sur"
                 if tab_texte[i+1]=="revenus" or tab_texte[i+1]=="revenu":    
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nbre_cas_contacts(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas" :
                if tab_texte[i+1]=="contact" or tab_texte[i+1]=="contacts":  
                #La nbre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nbre_cas_communautaire(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas":
                 if tab_texte[i+1]=="issus" or tab_texte[i+1]=="issu":  
                #La nbre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1])
    def get_nbre_cas_importes(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nbre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="importé" or tab_texte[i+1]=="importés":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nbre_gueris(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="patients" or tab_texte[i].lower()=="patient":
                #La nbre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="suivis" or tab_texte[i+1]=="suivi":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nbre_deces(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="décés":
                #La nbre vient apre le premier mot "Sur"
                if (tab_texte[i-1].lower()=="aucun"):
                    tab_texte[i-1]="0"
                return int(tab_texte[i-1]) 
    def get_nbre_cas_graves(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="cas" or tab_texte[i].lower()=="cas":
                #La nbre vient apre le premier mot "Sur"
                if tab_texte[i+1]=="graves" or tab_texte[i+1]=="grave":  
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
    def get_nbre_vaccines(self,texte):
        tab_texte=texte.split()
        for i in range(len(tab_texte)):
            if tab_texte[i].lower()=="personnes" or tab_texte[i].lower()=="personne":
                if "vaccinées" or "vaccinée" in tab_texte[i:i+6]:
                    #La nbre vient apre le premier mot "Sur"
                    if (tab_texte[i-1].lower()=="aucun"):
                        tab_texte[i-1]="0"
                    return int(tab_texte[i-1]) 
        
        
DE = DataExtraction()
print(DE.get_nbre_vaccines(text1))
print(DE.get_nbre_gueris(text1))
print(DE.get_nbre_cas_contacts(text1))

            
