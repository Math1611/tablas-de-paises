from flask import Flask, render_template

app = Flask (__name__)

# Lista de diccionario con la informacion de los paises.
paises = [{'pais': 'Argentina' , 'capital': 'Buenos Aires'},
    {'pais': 'Brasil' , 'capital': 'Brasilia'},
    {'pais': 'Chile' , 'capital': 'Santiago de Chile'},
    {'pais': 'Colombia' , 'capital': 'Bogotá'},
    {'pais': 'Costa Rica' , 'capital': 'San José'},
    {'pais': 'Paraguay' , 'capital': 'Asunción'},
    {'pais': 'Perú' , 'capital': 'Lima'}
]

@app.route('/')
def mostrar_paises():
    """Ruta principal que renderiza la planilla del index.html 
    y le pasa la lista de paises
    """
    
    return render_template('index.html', paises=paises)



if __name__ == '__main__':
    app.run(debug = True) # este permite cargar el servidor sin que se caiga reiteradas veces