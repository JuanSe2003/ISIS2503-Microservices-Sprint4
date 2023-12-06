from flask import Flask, render_template, url_for, redirect
from pymongo import MongoClient
from forms import PacienteForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

client = MongoClient("mongodb://pacientes_user:isis2503@10.128.0.3:27017")

db = client.pacientes_user
pacientes = db.pacientes

@app.route('/pacientes')
def show_pacientes():
    pacientes_list = [paciente for paciente in pacientes.find()]

    return render_template('pacientes.html', pacientes=pacientes_list)


@app.route('/pacientecreate', methods=['GET', 'POST'])
def paciente_create():
    form = PacienteForm()
    if form.validate_on_submit():
        pacientes.insert_one({
            "nombre": form.nombre.data,
            "correo": form.correo.data,
            "cc": form.cc.data,
            "plan_Salud": form.plan_Salud.data
        })
        return redirect(url_for('show_pacientes'))
    return render_template('paciente_create.html', form=form)
