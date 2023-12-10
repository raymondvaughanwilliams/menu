#models.py
from unicodedata import name
from structure import db,login_manager,app,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager
from datetime import datetime

# class UserTherapySession(db.Model):
#     __tablename__ = 'usertherapysessions'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User", foreign_keys=user_id)
#     booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))


class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    name = db.Column(db.String(64),nullable=True)
    last_name = db.Column(db.String(64),nullable=True)
    password_hash = db.Column(db.String(128))
    number = db.Column(db.String(128))
    location = db.Column(db.String(128))
    role = db.Column(db.String,nullable=True)
    phone_number = db.Column(db.String)
    # biography = db.Column(db.String)
    status=db.Column(db.String,default="unverified")



    # roles = db.relationship('Roles', secondary='user_roles')


    def __init__(self,email,username,password,name,role,last_name,number):
        self.email = email
        self.username = username
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.role = role
        self.last_name = last_name
        self.number = number
   

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"



# class Issue(db.Model):
#     __tablename__ = 'issues'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User", foreign_keys=[user_id])
#     organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
#     organization = db.relationship("Organization", foreign_keys=[organization_id])
#     title = db.Column(db.String(120))
#     description = db.Column(db.String(120))
#     location = db.Column(db.String(120))
#     contact = db.Column(db.String(120))
    
#     image1 = db.Column(db.String(120))
#     image2 = db.Column(db.String(120))
#     image3 = db.Column(db.String(120))
#     image4 = db.Column(db.String(120))
#     views = db.Column(db.Integer,default=0)
#     # likes = db.Column(db.Integer)
#     date = db.Column(db.Date)
#     likes_entries = db.relationship('LikeDislike', backref='issues', lazy=True)

#     def __init__(self,user_id,organization_id,title,description,location,contact,date):
#         self.user_id = user_id
#         self.organization_id = organization_id
#         self.title = title
#         self.description = description
#         self.location = location
#         self.contact = contact
#         self.date = date
#         # self.likes = likes

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))


class Food(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Integer())
    category = db.Column(db.String(120))
    # location = db.Column(db.String(120))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship("Restaurant", foreign_keys=[restaurant_id])
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", foreign_keys=[category_id])  
    
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    bio = db.Column(db.String(120))
    location = db.Column(db.String(120))
    contact1 = db.Column(db.String(120))
    contact2 = db.Column(db.String(120))
    contact3 = db.Column(db.String(120))
    image1 = db.Column(db.String(120))
    image2 = db.Column(db.String(120))
    image3 = db.Column(db.String(120))
    views = db.Column(db.Integer,default=0)
    # likes = db.Column(db.Integer)
    date = db.Column(db.Date)
    # likes_entry = db.relationship('LikeDislike', backref='restaurants', lazy=True)
    favorites_entry = db.relationship('Favorite', backref='restaurants', lazy=True)


# class Organization(db.Model):

#     __tablename__ = 'organizations'

#     id = db.Column(db.Integer,primary_key=True)
#     profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
#     location = db.Column(db.String(64))
#     description = db.Column(db.String(254))
#     workhours = db.Column(db.String(254))
#     attachment1 = db.Column(db.String(254))
#     attachment2 = db.Column(db.String(254))
#     likes = db.Column(db.String(254))
#     disklikes = db.Column(db.String(254))
#     views = db.Column(db.String(254))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User", foreign_keys=[user_id])    
#     status=db.Column(db.String,default="unverified")
#     likes_entries = db.relationship('LikeDislike', backref='organizations', lazy=True)

    

# class IssueComment(db.Model):
#     __tablename__ = 'issuecomments'
#     id = db.Column(db.Integer, primary_key=True)
#     issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'))
#     issue = db.relationship("Issue", back_populates="issuecomments")
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User")
#     parent_comment_id = db.Column(db.Integer, db.ForeignKey('issuecomments.id'))
#     parent_comment = db.relationship("IssueComment", remote_side=[id])
#     content = db.Column(db.String(255))
#     date = db.Column(db.Date)

#     # roles = db.relationship('Roles', secondary='user_roles')

# Issue.issuecomments = db.relationship("IssueComment", back_populates="issue", cascade="all, delete-orphan")



# class Discussion(db.Model):
#     __tablename__ = 'discussions'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     content = db.Column(db.String(255))
#     comments = db.relationship("DiscussionComment", back_populates="discussion", cascade="all, delete-orphan")
#     views = db.Column(db.Integer)
#     likes = db.Column(db.Integer)
#     dislikes = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User", foreign_keys=[user_id]) 
#     organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
#     organization = db.relationship("Organization", foreign_keys=[organization_id])
#     likes_entries = db.relationship('LikeDislike', backref='discussions', lazy=True)

# class DiscussionComment(db.Model):
#     __tablename__ = 'discussioncomments'
#     id = db.Column(db.Integer, primary_key=True)
#     discussion_id = db.Column(db.Integer, db.ForeignKey('discussions.id'))
#     discussion = db.relationship("Discussion", back_populates="comments")
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User")
#     parent_comment_id = db.Column(db.Integer, db.ForeignKey('discussioncomments.id'))
#     parent_comment = db.relationship("DiscussionComment", remote_side=[id])
#     content = db.Column(db.String(255))
#     date = db.Column(db.Date)
#     replies = db.relationship("DiscussionComment", back_populates="parent_comment", cascade="all, delete-orphan")



# class Poll(db.Model):
#     __tablename__ = 'polls'
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(255))
#     options = db.relationship("PollOption", back_populates="poll", cascade="all, delete-orphan")
#     votes = db.relationship("PollVote", back_populates="poll", cascade="all, delete-orphan")
#     likes_entries = db.relationship('LikeDislike', backref='polls', lazy=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User")

# class PollOption(db.Model):
#     __tablename__ = 'polloptions'
#     id = db.Column(db.Integer, primary_key=True)
#     poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
#     poll = db.relationship("Poll", back_populates="options")
#     option_text = db.Column(db.String(255))

# class PollVote(db.Model):
#     __tablename__ = 'pollvotes'
#     id = db.Column(db.Integer, primary_key=True)
#     poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
#     poll = db.relationship("Poll", back_populates="votes")
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User")
#     option_id = db.Column(db.Integer, db.ForeignKey('polloptions.id'))
#     option = db.relationship("PollOption")


# class LikeDislike(db.Model):
#     __tablename__ ="likes"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     likeable_id = db.Column(db.Integer, nullable=False)
#     likeable_type = db.Column(db.String(50), nullable=False)
#     value = db.Column(db.Integer, nullable=False)
#     poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
#     poll = db.relationship('Poll', backref='like_entries')
#     issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'))
#     issue = db.relationship('Issue', backref='like_entries')
#     discussion_id = db.Column(db.Integer, db.ForeignKey('discussions.id'))
#     discussion = db.relationship('Discussion', backref='like_entries')
#     organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
#     organization = db.relationship('Organization', backref='like_entries')
#     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
#     restaurant = db.relationship('Restaurant', backref='like_entries')


class Favorite(db.Model):
    __tablename__ ="favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    likeable_id = db.Column(db.Integer, nullable=False)
    likeable_type = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))
    food = db.relationship('Food', backref='favorite_e')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship('Restaurant', backref='favorite_e')


# class Upload(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(255), nullable=False)
#     issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'))
#     issue = db.relationship('Issue', backref=db.backref('uploads', lazy=True))
#     organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
#     organization = db.relationship('Organization', backref=db.backref('uploads', lazy=True))
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurants = db.relationship("Restaurant", back_populates="comments")
    content = db.Column(db.String(255))
    date = db.Column(db.Date)

    # roles = db.relationship('Roles', secondary='user_roles')

Restaurant.comments = db.relationship("Comment", back_populates="restaurants", cascade="all, delete-orphan")



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
