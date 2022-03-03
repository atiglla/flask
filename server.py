from flask import Flask,render_template#importamos la clase flask

app=Flask(__name__) #creando una instancia de clase app llamada name, siempre

@app.route('/') #En la ruta / me va a ajecutar la funcion que vaya en la siguiente linea
def holaMundo():
    return "¡Hola Mundo!"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"

@app.route ("/say/<usuario>")
def usuario (usuario):
        if type(usuario)==str:  
                return "¡Hola, "+(usuario.capitalize())+"!"  

@app.route ("/repeat/<int:numero>/<palabra>")
def repetir (numero,palabra):
    if (type(numero)==int and type(palabra)==str):
        return (palabra+" ")*int(numero)
    


if __name__=="__main__":#Asegurando de que el archivo se esta ejecutando directamente y no desde otro modulo
    app.run(debug=True)#Ejecuto mi aplicacion

