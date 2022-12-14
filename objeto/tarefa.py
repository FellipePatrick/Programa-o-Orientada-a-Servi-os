import requests

api_url = "http://jsonplaceholder.typicode.com"

class Tarefa:
    
    def __init__(self) -> None:
        pass
   
    def criar_t(id, dicionario):
        url = api_url +'/users/'+str(id)+'/todos'
        todo = dicionario
        response = requests.post(url, json=todo)
        return response.json()
   
    def ver_t(id):
        url = api_url +"/todos/"+str(id)+ "/todos/"
        responsecheck = requests.get(url)
        response = requests.get(url).json()
        if responsecheck.status_code == 200:
            for task in response:
                print('Título: ', task['title'])
                print('ID', task['id'])
    
    def delete_t(id):
        url = api_url +"/todos/" + str(id)
        response = requests.delete(url)
        return response.json()
        
    def atualizar_t(id, dicionario):
        url = api_url +'/todos/'+ str(id)
        todo = dicionario
        response = requests.put(url, json=todo)
        return response.json()        
