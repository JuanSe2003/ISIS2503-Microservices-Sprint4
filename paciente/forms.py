from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PacienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    cc = IntegerField('Cédula de Ciudadanía')
    plan_Salud = StringField('Plan de Salud')
    submit = SubmitField('Create')
