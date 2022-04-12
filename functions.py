import re
from difflib import SequenceMatcher

def similar(a, b):
   return SequenceMatcher(None, a, b).ratio()


def extractActivité(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Activité", word)>0.8):
        
        raisonsociel=re.search(": [A-Za-z ]+",text[i])
        raisonsociel=raisonsociel[0].replace(": ","")
        
        return raisonsociel
        
        
        
def form(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Formo", word)>0.8):
        
        raisonsociel=re.search(": [A-Za-z -À]+",text[i])
        raisonsociel=raisonsociel[0].replace(": ","")
        try:

          return raisonsociel
        except:
          print("")
          
          
def siege(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Siège ", word)>0.8):
        
        raisonsocial=re.search(": [A-Za-z -Àé]+",text[i])
        
        raisonsocial=raisonsocial[0].replace(": ","")
        try:

          return raisonsocial
        except:
          print("")
          
def extractnom(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Dénomination", word)>0.8):
        nom=re.search(": [A-Za-z]+ [A-Za-z]+",text[i])
        nom=nom[0].replace(": ","")
  try:
       return nom
  except :
        print("none")
          
          
def Capital(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Capital ", word)>0.8):
        
        Capital=re.search(": [A-Za-z 0-9 .]+|; [A-Za-z 0-9 .]+",text[i])

        
        try:
          Capital=Capital[0].replace("; ","")
          Capital=Capital.replace(": ","")  
          return Capital
        except:
          print("")
          
          
def date(text):
  for i in range(len(text)-1):
    temp = text[i].split(" ")  
    for word in temp :
      if(similar("Date", word)>0.8 or similar("immatriculation ", word) > 0.8 ):
        
        date=re.search(": [0-9 /]+",text[i])
        try:
          date=date[0].replace("; ","")
          date=date.replace(": ","")
          date=date.replace(" ","")
        
                      
          return date
          break
        except:
          print("")
    
          
          
