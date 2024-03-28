from flask import Flask

app = Flask(__name__)

@app.route(/)
def registro_producto():
    head = '<h1>Registrar productos</h1>'
    nombre_producto = '<br><input type="text" id="nombre_producto" name="nombre_producto" requerid placeholder="Nombre del producto"><br>'
    precio_producto = '<br><input type="number" id="precio_producto" name="precio_producto" requerid placeholder="Precio del producto"><br>'
    cantidad_producto = '<br><input type="number" id="cantidad_producto" name="cantidad_producto" requerid placeholder="Cantidad del producto><br>"'
    enviar = '<br><input type="submit" value="Registrar">'
    return (
         head +
         'Nombre del productoo:' + nombre_producto +
         'Precio del producto:' + precio_producto +
         'Cantidad deel producto:' + cantidad_producto +
         enviar
    )
if __name__ == '__main__':
    app.run(debug=True)

