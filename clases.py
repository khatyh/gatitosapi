import requests #Estoy importando la libreria requests que me sirve para comunicarme con la api
from skimage import io
from PIL import ImageTk,Image
import os

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
        2.-Salir
        ===================================
        """)
        op=input("Seleccionar Opcion: ")
        if op == "1":
            Main.imagenes()
        elif op == "2":
            os._exit()
        else:
            print("Error elija solo las opciones en pantalla")
            input("Presione ENTER para continuar")