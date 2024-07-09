from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField,RadioField,SelectField,DecimalField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class CheckupForm(FlaskForm):

    username=StringField('Name',validators=[DataRequired(),Length(max=100)])
    gender=RadioField('Gender',validators=[DataRequired()],choices=['Male','Female','Others'])
    age=IntegerField('Age',validators=[DataRequired()])
    address=StringField('Address',validators=[DataRequired(),Length(max=250)])
    pincode=IntegerField('Pincode',validators=[DataRequired()])
    hypertension=RadioField('Hypertension',validators=[DataRequired()],choices=['Yes','No'])
    previousHeartDisease=RadioField('Previous Heart Disease',validators=[DataRequired()],choices=['Yes','No'])
    smoking_History=SelectField("Smoking History",validators=[DataRequired()],choices=[('never','Never'),('former','Former'),('current','Current'),('notcurrent','Not Current'),('ever','Ever'),('other','Other')])
    weight=DecimalField("Weight (in kg)",validators=[DataRequired()],places=2)
    height=DecimalField("Height (in m)",validators=[DataRequired()],places=2)
    hba1clvl=SelectField("HbA1c Level",validate_choice=[DataRequired()],choices=[('3below','below 3'),('34','3-4'),('45','4-5'),('56','5-6'),('67','6-7'),('78','7-8'),('89','8-9'),('9above','above 9')])
    blood_glucose=IntegerField('Blood Glucose Level',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email(),Length(max=50)])
    phone=IntegerField('Phone Number',validators=[DataRequired()])
    submit=SubmitField('Submit')