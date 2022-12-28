import requests #Estoy importando la libreria requests que me sirve para comunicarme con la api
from skimage import io
from PIL import ImageTk,Image
import os
import json
class Variables:
    url=""
class Main:

    def __init__(self) -> None:
        pass

    def imagenes():
        Headers = { 'x-api-key' : 'live_DHPHw5H2c54o4EmTM88MKSxoWb121gkyW0ugTo4yjYt6rtk4GdItFk15CNWhpnui' }
        response = requests.get('https://api.thecatapi.com/v1/images/search', headers=Headers)

        api_key="live_DHPHw5H2c54o4EmTM88MKSxoWb121gkyW0ugTo4yjYt6rtk4GdItFk15CNWhpnui"
        r = requests.get('https://api.thecatapi.com/v1/images/search') 

        datos = r.json()

        gato=datos[0]["url"]

        url_imagen = gato # El link de la imagen
        Variables.url=url_imagen
        nombre_local_imagen = "gatotemp.jpg" # El nombre con el que queremos guardarla
        imagen = requests.get(url_imagen).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)
            
        image = io.imread("gatotemp.jpg")
        io.imshow(image)
        io.show()

    def menu(self):
        os.system("cls")
        print("""
        ================MENU===============
        1.-Mostrar Gatito
        2.-Mostrar Favoritos
        3.-Editar Favoritos
        4.-Borrar Favorito
        0.-Salir
        ===================================
        """)
        op=input("Seleccionar Opcion: ")

        if op == "1":
            Main.imagenes()
            url="http://localhost:5000/gatos"
            print(Variables.url)
            payload={"link":Variables.url}
            headers ={"Content-Type":"application/json"}
            response= requests.post(url,json=payload,headers=headers)
            
        elif op == "2":
            
            response = requests.get(f"http://localhost:5000/gatos")

            if response.status_code == 200:
                gatito = response.json()
                print(gatito)
            else:
                print("Gatito no encontrado")
            input()
        elif op == "3":

            nombre_gatito = input("Que nombre desea modificar?...\n")
            nom=input("Ingrese nuevo nombre\n")
            col=input("Ingrese nuevo color\n")
            ed=input("Ingrese nueva edad\n")
            data = {
                "nombre": nom,
                "color": col,
                "edad": ed
            }

            response = requests.put(f"http://localhost:5000/gatos/{nombre_gatito}", json=data)

            if response.status_code == 200:
                gatito = response.json()
                print(gatito)
                print("Se ha editado exitosamente...")
                
            else:
                print("Gatito no encontrado")

            input()
        elif op == "4":
            nombre_gatito =input("Ingrese el nombre del gato que desea borrar...\n")

            response = requests.delete(f"http://localhost:5000/gatos/{nombre_gatito}")

            if response.status_code == 200:
                gatitos = response.json()
                print(gatitos,"Se ha eliminado correctamente...")
                
            else:
                print("Gatito no encontrado")
            input()
        elif op == "0":
            os._exit()
        else:
            print("Error elija solo las opciones en pantalla")
            input("Presione ENTER para continuar")