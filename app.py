from flask import Flask, render_template, request, redirect , url_for, flash

app = Flask(__name__)

from database import app, db, EmpleadoSchema
from empleado import Empleado

student_schema = EmpleadoSchema()
students_schema = EmpleadoSchema(many=True)

@app.route('/')
def index():
    todosEmpleados = Empleado.query.all()
    return render_template('index.html', empleados = todosEmpleados)

@app.route('/insertar',methods = ['POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']

        empleado = Empleado(nombre,email,telefono)
        db.session.add(empleado)
        db.session.commit()

        flash('Empleado añadido correctamente')
        
        return redirect(url_for('index'))

@app.route('/editar',methods = ['GET','POST'])
def editar():
    if request.method == 'POST':
        empleado = Empleado.query.get(request.form.get('id'))
        
        empleado.nombre = request.form['nombre']
        empleado.email = request.form['email']
        empleado.telefono = request.form['telefono']

        db.session.commit()
        flash('Empleado actualizado correctamente')

        return redirect(url_for('index'))

@app.route('/eliminar/<id>',methods=['GET','POST'])
def eliminar(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    flash('Empleado eliminado correctamente')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
