import functions

# Telechargement de tous les fichiers disponibles au niveau du site du ministére en effectuant on the fly leur transformation en fichier text
url = 'https://sante.sec.gouv.sn/sites/default/com'

extension = '_covid19.pdf'
for i in range(start=92,stop=103): #Recuperation des communiques du numero start à stop

    try:
        functions.downloadFile(url+str(i)+'_covid19.pdf')
        functions.transformPDFToText("com"+{str(i)}+extension)
    except:
        try:
            functions.downloadFile(url+str(i)+'covid19.pdf')
            functions.transformPDFToText("com"+{str(i)}+extension)

        except:
            try:
                functions.downloadFile(url+str(i)+'_covid-19.pdf')
                functions.transformPDFToText("com"+{str(i)}+extension)

            except:
                pass
