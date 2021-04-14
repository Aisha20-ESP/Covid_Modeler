import twint


# Configure
c = twint.Config()
c.Username="MinisteredelaS1"
c.Output = "ImagesCommunique.csv"
c.Store_csv = True
c.Images=True
#run
twint.run.Search(c)


#Mettre les liens des  images dans une liste 
import csv
liste=[]
with open('ImagesCommunique.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    #  print(row['thumbnail'])
     liste.append(row['thumbnail'])



# Telecharger L'image et le mettre dans le dossier ImagesCommuniques en le renommer
import urllib.request
for i in range(1 ,514):    
     urllib.request.urlretrieve(liste[i] ,"./ImagesCommuniques/communique"+str(i)+".jpg")
     print("Picture Download with Success")





