#importaciones de librerias y framework
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

#importacion de modelos
from Models.Conexion import * 



#Configuracion en el CORS
CORS(app, resources={
    r"/*": {"origins": "*"},
    r"/*": {
        "origins": ["*"],
        "methods": ["OPTIONS", "POST", "PUT", "GET", "DELETE"],
        "allow_headers": ["Authorization", "Content-Type", "id_mesa"],
        }
    })

#importacion de rutas
from Routes.Routes import *

#Reglas de rutas Suport
app.add_url_rule(suport["qrcode"], view_func=suport["qrcodecontrollers"])

app.add_url_rule(user["register_user"], view_func=user["register_user_controllers"])
 
app.add_url_rule(admin["login_admin"], view_func=admin["login_admin_controllers"])

app.add_url_rule(menu["listar_menu"], view_func=menu["listar_menu_controllers"])

app.add_url_rule(crearMenu["crear_menu"], view_func=crearMenu["crear_menu_controllers"])

app.add_url_rule(mandarMenu["mandar_menu"], view_func=mandarMenu["mandar_menu_controllers"])

app.add_url_rule(editarMenu["editar_menu"], view_func=editarMenu["editar_menu_controllers"])

app.add_url_rule(eliminarMenu["eliminar_menu"], view_func=eliminarMenu["eliminar_menu_controllers"])

app.add_url_rule(agregarCarrito["agregar_carrito"], view_func=agregarCarrito["agregar_carrito_controllers"])

app.add_url_rule(eliminarCarrito["eliminar_carrito"], view_func=eliminarCarrito["eliminar_carrito_controllers"])

app.add_url_rule(resultadosCarrito["resultados_carrito"], view_func=resultadosCarrito["resultados_carrito_controllers"])

app.add_url_rule(CarritoCompras["carrito_compras"], view_func=CarritoCompras["carrito_compras_controllers"])




if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True,port=5000)