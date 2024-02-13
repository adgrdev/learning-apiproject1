from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
## Start the server with: python3 -m uvicorn users:app --reload

@app.get("/")
async def root():
    return "Main page"

#User entity
class User(BaseModel): #BaseModel help us to create an entity
    id: int
    name: str
    lastname: str
    age: int

## Simulamos una DB con una lista
users_list = [User(id = 1, name = "Elena", lastname = "Gutierrez", age = 7),
         User(id = 2, name = "Ciro", lastname = "Herrera", age =  8),
         User(id = 3, name = "Capi", lastname = "Guti", age = 1 ),
         User(id = 4, name = "Orion", lastname = "Palace", age = 6 ),
         ]

''' 
@app.get("/userslocal")
async def userslocal():
    return [{"name": "Elena", "lastname": "Gutierrez", "age": 7},
            {"name": "Ciro", "lastname": "Herrera", "age": 8}]
'''


@app.get("/users")
async def users():
    return users_list

#Function to get user by id
#Esta función trabaja con un parametro en el path, lo que significa que se llama
#desde la propio url (Para otro  caso ver proxima función)

'''
@app.get("/user/{id}")
async def user(id: int): #Creamos una nueva función user y se define el tipo de dato que le enviamos
    #HOF Filter
    users = filter (lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}
'''
@app.get("/user/{id}") #Igualamos una clave con un valor en la URL
async def user(id: int):
    return search_user(id)
    
#Funcion para obtener usuarios por ID
#en esta ocasión usando la query
    
@app.get("/user/") #Igualamos una clave con un valor en la URL
async def user(id: int): #Agrego parametro de busqueda
    return search_user(id)
    
'''
Podria agregar dos parametros de busqueda co
async def user(id: int, name: str):

en la busqueda, la url seria: ?id=1&name=ciro
'''
#Generalizo con una funcion search_user
def search_user(id: int):
    users = filter (lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}