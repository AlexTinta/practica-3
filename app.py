from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mi_secreto'  # Necesario para utilizar session

# Página de inicio con el formulario de registro
@app.route('/')
def registro():
    return render_template('registro.html')

# Ruta para procesar el formulario de registro
@app.route('/registrar', methods=['POST'])
def registrar():
    fecha = request.form.get('fecha')
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    turno = request.form.get('turno')
    seminarios = request.form.getlist('seminarios')  # Lista de seminarios seleccionados

    # Almacenamos los datos en la sesión
    if 'inscritos' not in session:
        session['inscritos'] = []

    session['inscritos'].append({
        'fecha': fecha,
        'nombre': nombre,
        'apellidos': apellidos,
        'turno': turno,
        'seminarios': ', '.join(seminarios)  # Convertir la lista a cadena
    })

    return redirect(url_for('lista'))

# Ruta para mostrar la lista de inscritos
@app.route('/lista')
def lista():
    inscritos = session.get('inscritos', [])
    return render_template('lista.html', inscritos=inscritos)

# Ruta para eliminar un inscrito
@app.route('/eliminar/<int:index>')
def eliminar(index):
    inscritos = session.get('inscritos', [])
    if inscritos and index < len(inscritos):
        inscritos.pop(index)
        session['inscritos'] = inscritos
    return redirect(url_for('lista'))

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
