import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = "pokytester"
password = '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'

 
p = str(input('deletar, ver meus, seguir, checar:'))
 
if p == 'deletar':
    response = requests.delete('https://api.github.com/user/following'+'/DUARTEzinho',
        auth = HTTPBasicAuth(user, password))

elif p == 'ver meus':
    response = requests.get('https://api.github.com/user/followers',
        auth = HTTPBasicAuth(user, password))
 
elif p == 'seguir':
    response = requests.put('https://api.github.com/user/following'+'/DUARTEzinho',
        auth = HTTPBasicAuth(user, password))

elif p == 'checar':
    response = requests.get('https://api.github.com/users/dvcirilo/following/maikerosa',
        auth = HTTPBasicAuth(user, password))
 
  
print(response[('login')])

print(response)