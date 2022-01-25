#Anastasia Avilova, Jūlija Kuļikovska, Artūrs Kalniņš, Maksims Klaģišs, Tatjana Karpenkova
text = input( "Ievadiet tekstu: ")
def deleteE(text):
  if text.count("e")>0:
    text = text.replace("e"," ")
    text = text.upper()
    print(text)
  else:
    text = "TEKSTS NESATUR VAJADZĪGO BURTU."
    print(text)
  return text
deleteE(text)