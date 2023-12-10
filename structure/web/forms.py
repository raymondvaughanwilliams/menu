# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField , SelectField , FormField, FieldList
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    food_name = StringField('Food Name')
    restaurant_name = StringField('Restaurant Name')
    type = SelectField('Type',validators=[DataRequired()],choices=[('restaurant', 'Restaurant'), ('food', 'Food')])
    min_price = DecimalField('Min Price')
    max_price = DecimalField('Max Price')
    submit = SubmitField('Apply Filters')


class FoodForm(FlaskForm):
    name = StringField('Food Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])

class AddFoodsForm(FlaskForm):
    restaurant = SelectField('Restaurant', coerce=int, validators=[DataRequired()])
    foods = FieldList(FormField(FoodForm), min_entries=2)
    submit = SubmitField('Add Foods')