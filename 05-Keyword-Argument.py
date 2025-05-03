

'''
-> Esma chai Hamilai Kati ota key-value pair pathauchau bhanne tha hudaina Dictionary ma

'''

def keyword_arguments(**kwargs):
  for key , value in kwargs.items():
    print(f" Key: {key} Value : {value} \n")
    
myDict = {
  "name":"Ujjwal",
  "location":"Jhumka"
}

keyword_arguments(**myDict)