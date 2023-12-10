from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField,FileAllowed


class AboutForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Title', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    feature_subtitle = StringField('Feature Subtitle', validators=[DataRequired()])
    feature_paragraph = StringField('Feature Paragraph', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    contact_subtitle = StringField('Contact Subtitle', validators=[DataRequired()])
    about_image = FileField('Update About Picture', validators=[FileAllowed(['jpg', 'png'])])
    about_subtitle = StringField('About Subtitle', validators=[DataRequired()])
    faq_title = StringField('Faq Title', validators=[DataRequired()])
    faq_subtitle = StringField('Faq Subtitle', validators=[DataRequired()])
    faq_paragraph = StringField(' Faq Paragraph', validators=[DataRequired()])
    testimonial_title = StringField('Testimonial title', validators=[DataRequired()])
    testimonial_subtitle = StringField('Testimonial Subtitle', validators=[DataRequired()])
    testimonial_paragraph = StringField('Testimonial paragraph', validators=[DataRequired()])
    team_title = StringField('Team Title', validators=[DataRequired()])
    team_subtitle = StringField('Team Subtitle', validators=[DataRequired()])
    team_paragraph = StringField('Team Paragraph', validators=[DataRequired()])
    carousellink = StringField('Firebase Link')
    aboutimagelink = StringField('Firebase Link')
    link3 = StringField('Firebase Link')
    logo = FileField('Update Logo', validators=[FileAllowed(['jpg', 'png'])])
    menu = FileField('Upload File', validators=[FileAllowed(['jpg', 'png'])])
    carousel_image_1 =FileField('Update Banner Image', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')





class UpdateAboutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Email()])
    text = StringField('Text', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    contact_subtitle = StringField('Contact Subtitle', validators=[DataRequired()])
    about_subtitle = StringField('About Subtitle', validators=[DataRequired()])
    feature_subtitle = StringField('Feature Subtitle', validators=[DataRequired()])
    feature_paragraph = StringField('Feature Paragraph', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    faq_title = StringField('Faq Title', validators=[DataRequired()])
    faq_subtitle = StringField('Faq Subtitle', validators=[DataRequired()])
    faq_paragraph = StringField(' Faq Paragraph', validators=[DataRequired()])
    testimonial_title = StringField('Testimonial title', validators=[DataRequired()])
    testimonial_subtitle = StringField('Testimonial Subtitle', validators=[DataRequired()])
    testimonial_paragraph = StringField('Testimonial paragraph', validators=[DataRequired()])
    team_title = StringField('Team Title', validators=[DataRequired()])
    team_subtitle = StringField('Team Subtitle', validators=[DataRequired()])
    team_paragraph = StringField('Team Paragraph', validators=[DataRequired()])
    about_picture = FileField('Update About Picture', validators=[FileAllowed(['jpg', 'png'])])
    carousellink = StringField('Firebase Link')
    aboutimagelink = StringField('Firebase Link')
    link3 = StringField('Firebase Link')
    logo = FileField('Update Logo', validators=[FileAllowed(['jpg', 'png'])])
    carousel_image_1 =FileField('Update Banner Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

