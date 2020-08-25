from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    unit = StringField('unit', validators=[DataRequired()])
    unit_price = DecimalField('unit_price', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])

class ProductSaleForm(FlaskForm):
    quantity = IntegerField('quantity', validators=[DataRequired()])