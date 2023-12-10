from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, HiddenField,FloatField,IntegerField,SubmitField,SelectField,SelectMultipleField,TextAreaField,FileField,Form,DateTimeField,TimeField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField,DateTimeField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo ,Length
from wtforms import ValidationError
from wtforms_components import TimeField



class IssueForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Email()])
    # company = StringField('Company Name', [validators.Length(min=4, max=25)])
    date = DateField('Choose Date', [validators.DataRequired()] ,format='%Y-%m-%d')
    organization = StringField('Organization')
    contact = StringField('Contact')
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    description = TextAreaField('Description', [validators.Length(min=4, max=140)]) 
    location = StringField('Location',[validators.Length(min=4,max=140)])
    time= TimeField('Time', [validators.DataRequired()])
    submit = SubmitField('BOOK THERAPIST')


class UpdateSessionForm(FlaskForm):
    date = DateField('Choose Date', [validators.DataRequired()], format='%Y-%m-%d')
    time = TimeField('Time',[validators.DataRequired()])
    submit = SubmitField('Reschedule')



class ResultForm(FlaskForm):
    name = StringField('Text', [validators.DataRequired()])
    subject = StringField('Text')
    result = IntegerField('Result')
    index_number = StringField('Index Number')

    # subject= SelectField('Subject')
    year = SelectField('Year', choices=[(str(year), str(year)) for year in range(2023, 2034)])
    submit = SubmitField('Add')

class StudentForm(FlaskForm):
    name = StringField('Text', [validators.DataRequired()])
    subject = StringField('Text')
    index_number = StringField('Index Number')
    year = SelectField('Year', choices=[(str(year), str(year)) for year in range(2023, 2034)])
    submit = SubmitField('Add')


class SipRequestForm(FlaskForm):
    channels = StringField('Text', [validators.DataRequired()])
    ip = StringField('IP', [validators.DataRequired()])
    create_extension = SelectField('Inbound',validators=[DataRequired()],choices=[('yes', 'Yes'), ('no', 'No')])
    other = TextAreaField('Text')
    codecs = StringField('Codecs')
    status = SelectField('Status',validators=[DataRequired()],choices=[('verified', 'Verified'), ('unverified', 'Unverified')])
    certificate = FileField('Certificate', validators=[ FileAllowed(['jpg','png','gif','jpeg'])])
    inbound = SelectField('Inbound',validators=[DataRequired()],choices=[('yes', 'Yes'), ('no', 'No')])
    outbound = SelectField('Outbound',validators=[DataRequired()],choices=[('yes', 'Yes'), ('no', 'No')])
    provider = SelectField('Provider',validators=[DataRequired()],choices=[('mtn', 'MTN'), ('vodafone', 'Vodafone')])
    ratecard = SelectField('Provider',validators=[DataRequired()],choices=[('MTN O.15 Termination', 'MRH1-zAeN'), ('Vodafone 0.16 Termination', '7M8u-2Pv'),('MTN International','mB_2-ijp6'),('Vezeti','ytV2-Kjbn')])
    submit = SubmitField('Add')

    
class NewsletterForm(Form):
    name = StringField('Name')
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Join Newsletter')
    
    

    


    
    
    
class FilterForm(FlaskForm):
    # destination = SelectField("Destination", choices=[(destination.id, destination.name) for destination in destinations])
    # location = SelectField("Location", choices=[(destination.id, destination.name) for destination in destinations])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    number = StringField('Premium Amount')
    premium_amount = StringField('Premium Amount')
    location = StringField('Location')
    language = StringField('Language')
    country = StringField('Country')
    society = StringField('Society')
    cooperative = StringField('Cooperative')
    ordernumber = StringField('Order Number')
    submit = SubmitField('Submit') 
    
    
class ContactForm(Form):
    name = StringField('Name')
    email = StringField('Email', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    hidden = HiddenField('Hidden',default="contact" )
    submit = SubmitField('Submit')
   
   
class FarmerForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    number = StringField('Premium Amount')
    farmercode = StringField('Farmer Code')
    premium_amount = StringField('Premium Amount')
    location = StringField('Location')
    language = StringField('Language')
    country = StringField('Country')
    cooperative = StringField('Cooperative')
    ordernumber = StringField('Order Number')
    society = StringField('Society')
    cashcode = StringField('Cashcode')
    index_number = StringField('Index Number')
    uploadfile = FileField('Upload', validators=[FileRequired(), FileAllowed(['csv'])])
    submit = SubmitField('Submit') 
    
    
class RequestForm(Form):
    name = StringField('Name',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    model_year = StringField('Model Year', validators=[DataRequired()])
    car_make = StringField('Car Type', validators=[DataRequired()])
    car_model = StringField('Model ', validators=[DataRequired()])
    quantity = StringField('Quantity ', validators=[DataRequired()])
    note =  TextAreaField('Note', [validators.Length(min=4, max=140)]) 

    submit = SubmitField('Submit')
    
    
class BidForm(Form):
    price = IntegerField('Price',validators=[DataRequired()])
    quantity = StringField('Quantiy', validators=[DataRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField('Submit')
    
    
class ExtForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    ips = StringField('Ips', validators=[DataRequired()])



class NumberSearchForm(Form):
    country= SelectField('Country', validators=[DataRequired()],choices=[('ghana', 'Ghana'),('nigeria','Nigeria')])
    number = StringField('Number', validators=[DataRequired()])
    provider = SelectField('Provider', validators=[DataRequired()],choices=[('mtn', 'MTN'),('vodafone','Vodafone')])

    
class ReviewForm(Form):
    text = TextAreaField('Text', validators=[DataRequired()])
    hidden = HiddenField('Hidden', validators=[DataRequired()])
    submit = SubmitField('Submit')



class IVRForm(FlaskForm):
    account_id = IntegerField('Account ID', validators=[DataRequired()])
    customer_id = IntegerField('Customer ID', validators=[DataRequired()])
    dest = StringField('Destination', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    invalid_file = StringField('Invalid File', validators=[DataRequired()])
    file = FileField('File')
    key_0_destination = StringField('Key 0 Destination', validators=[DataRequired()])
    key_0_destination_type = SelectField('Key 0 Destination Type', choices=[('external', 'Phone Number'), ('internal', 'Digital receptionist')])
    key_1_destination = StringField('Key 1 Destination', validators=[DataRequired()])
    key_1_destination_type = SelectField('Key 1 Destination Type', choices=[('external', 'Phone Number'), ('internal', 'Digital receptionist')])
    key_2_destination = StringField('Key 2 Destination', validators=[DataRequired()])
    key_2_destination_type = SelectField('Key 2 Destination Type', choices=[('external', 'Phone Number'), ('internal', 'Digital receptionist')])
    key_3_destination = StringField('Key 3 Destination', validators=[DataRequired()])
    key_3_destination_type = SelectField('Key 3 Destination Type', choices=[('external', 'Phone Number'), ('internal', 'Digital receptionist')])
    submit = SubmitField('Submit')