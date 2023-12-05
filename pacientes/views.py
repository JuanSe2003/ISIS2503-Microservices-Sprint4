from flask import render_template, redirect, url_for, request
from app import app, db
from models import Paciente
from forms import PacienteForm

@app.route('/pacientes')
def paciente_list():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)

@app.route('/pacientecreate', methods=['GET', 'POST'])
def paciente_create():
    form = PacienteForm()
    if form.validate_on_submit():
        paciente = Paciente(nombre=form.nombre.data, correo=form.correo.data,
                            cc=form.cc.data, plan_Salud=form.plan_Salud.data)
        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for('paciente_list'))
    return render_template('paciente_create.html', form=form)
