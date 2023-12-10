import atexit
import csv
import os
from os import environ
from uuid import uuid4
import secrets
import random
import string
import requests
from requests.auth import HTTPBasicAuth
from apscheduler.schedulers.background import BackgroundScheduler
from flask import render_template, Blueprint, session, redirect, url_for, jsonify, current_app, request
from flask_login import login_required
from sqlalchemy import and_, or_, desc
from flask_mail import Mail, Message
from datetime import date,datetime
from structure import db,mail ,photos,app
from structure.core.forms import FilterForm,SipRequestForm , IssueForm,NumberSearchForm,ExtForm
from structure.about.forms import AboutForm
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract 
from io import BytesIO
import base64

core = Blueprint('core', __name__)



# @core.context_processor
# def utility_processor():
#     def get_option_percentage(poll_id, option_id):
#         total_votes = PollVote.query.filter_by(poll_id=poll_id).count()
#         option_votes = PollVote.query.filter_by(poll_id=poll_id, option_id=option_id).count()
#         return round((option_votes / total_votes) * 100, 2) if total_votes > 0 else 0

#     return dict(get_option_percentage=get_option_percentage)
# # def require_api_key(view_function):
# #     def decorated_function(*args, **kwargs):
# #         if request.headers.get('Authorization') == API_KEY:
# #             return view_function(*args, **kwargs)
# #         else:
# #             return jsonify({'error': 'Invalid API key', 'status': False}), 401

# #     return decorated_function


# def get_total_likes(likeable_model, likeable_id):
#     return LikeDislike.query.filter_by(likeable_type=likeable_model.__name__.lower(), likeable_id=likeable_id,value=1).count()

# def get_total_dislikes(likeable_model, likeable_id):
#     return LikeDislike.query.filter_by(likeable_type=likeable_model.__name__.lower(), likeable_id=likeable_id,value=0).count()


# allowed_extensions = ['png', 'jpg', 'jpeg', 'gif','txt','pdf']
# def check_file_extension(filename):
#     return filename.rsplit('.', 1)[1].lower() in allowed_extensions


# @core.route('/base')
# def base():
#     '''
#     Example view of any other "core" page. Such as a info page, about page,
#     contact page. Any page that doesn't really sync with one of the models.
#     '''
#     return render_template('base.html')

# @core.route('/issues')
# def issues():
#     polls = Poll.query.all()
#     organizations = Organization.query.all()
#     issues = Issue.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/issues.html', organizations = organizations,issues=issues,polls=polls,discussions=discussions)


# @core.route('/myissues')
# def myissues():
#     polls = Poll.query.all()
#     organizations = Organization.query.all()
#     myissues = Issue.query.filter_by(user_id=session['id']).all()
#     issues = Issue.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/myissues.html', organizations = organizations,issues=issues,polls=polls,discussions=discussions)


# @core.route('/discussions')
# def discussions():
#     discussions = Discussion.query.all()
#     polls = Poll.query.all()
#     issues = Issue.query.all()
#     organizations = Organization.query.all()
#     return render_template('portal/discussions.html', organizations = organizations,issues=issues,polls=polls,discussions=discussions)

# @core.route('/mydiscussions')
# def mydiscussions():
#     polls = Poll.query.all()
#     organizations = Organization.query.all()
#     mydiscussions = Discussion.query.filter_by(user_id=session['id']).all()
#     issues = Issue.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/mydiscussions.html', organizations = organizations,mydiscussions=mydiscussions,polls=polls,discussions=discussions,issues=issues)


# @core.route('/polls')
# def polls():
#     polls = Poll.query.all()
#     issues = Issue.query.all()
#     organizations = Organization.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/polls.html', organizations = organizations,issues=issues,polls=polls,discussions=discussions)

# @core.route('/mypolls')
# def mypolls():
#     polls = Poll.query.all()
#     organizations = Organization.query.all()
#     mypolls = Poll.query.filter_by(user_id=session['id']).all()
#     issues = Issue.query.all()
#     polls = Poll.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/mypolls.html', organizations = organizations,mypolls=mypolls,polls=polls,discussions=discussions,issues=issues)




# @core.route('/organizations')
# def organizations():
#     issues = Issue.query.all()
#     organizations = Organization.query.all()
#     polls = Poll.query.all()
#     discussions = Discussion.query.all()
#     return render_template('portal/organizations.html', organizations = organizations,issues=issues,polls=polls,discussions=discussions)

# @core.route('/')
# def home():
#     # user = User.query.filter_by(id=session['id']).first()
  
  
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     # session.pop('msg', None)
#     # api_url = 'https://app.connexcs.com/api/cp/customer?status=inactive'
#     # # response = requests.get(api_url)
#     # response = requests.get(api_url, headers=headers,auth=HTTPBasicAuth(connex_username, connex_password))
#     # inactive = response.json() if response.status_code == 200 else []
#     # # print(response.content)
 
    


#     return render_template(
#         'web/index.html',
         
#     )




# @core.route('/dashboard')
# # @login_required
# def dashboard():
#     issues = Issue.query.all()
#     discussions = Discussion.query.all()
#     organizations = Organization.query.all()
#     polls = Poll.query.all()
#     return render_template(
#         'portal/dashboard.html',issues=issues, discussions= discussions, organizations= organizations,polls=polls
         
#     )


# @core.route("/issues/new", methods=["GET", "POST"])
# def new_issue():
#     form = IssueForm()
#     organizations  = Organization.query.all()
#     # user = User.query.filter_by(id=session['id']).first()
    
#     if request.method == "POST":
#         # if request.files.get('image1'):
#         #     image1 = photos.save(request.files['image1'], name=secrets.token_hex(10) + ".")
#         #     image1= "static/uploads/issues/"+image1
#         #     print("image1")
#         #     print(image1)
        
#         print(form.description.data)
#         issue = Issue(user_id=session['id'],description= form.description.data,title = form.title.data,
#                        location = form.location.data,organization_id = form.organization.data ,date = datetime.now(),contact=form.contact.data
#                           )
#         db.session.add(issue)
#         db.session.commit()
#         uploaded_files = request.files.getlist('images')

#         # Process and save each uploaded file to the database
#         for img in uploaded_files:
#             # if img:
#             filename = secure_filename(img.filename)
#             print(filename)
#             # file.save(photos.config['UPLOADED_PHOTOS_DEST'] + '/' + filename)
#             image = photos.save(img, name=secrets.token_hex(10) + ".")
#             image= "static/uploads/issues/"+image

#             # Save file details to the database and associate with the issue
#             upload = Upload(filename=image, issue=issue, issue_id=issue.id)
#             db.session.add(upload)
#             db.session.commit()

  
#     return render_template("portal/newissue.html",form=form,organizations=organizations)


# @core.route('/issue/<int:issue_id>',methods=['GET', 'POST'])
# def issue(issue_id):
#     # form = NewsletterSubForm()
#     issue =  Issue.query.filter(Issue.id == issue_id).first()
#     issuecomments = IssueComment.query.filter_by(issue_id=issue_id, parent_comment_id=None).all()
#     issue.views =issue.views + 1
#     db.session.commit()
#     title = issue.title
#     related = Issue.query.all()
#     discussions = Discussion.query.all()
#     polls = Poll.query.all()
#     issues = Issue.query.all()
#     return render_template('portal/issue.html',issue=issue,title=title,issuecomments=issuecomments,related=related,discussions=discussions,polls=polls,issues=issues)


# @core.route('/issue/<int:issue_id>/add_comment', methods=['POST'])
# def add_comment(issue_id):
#     issue = Issue.query.get(issue_id)
#     user_id = 3  # Replace with the actual user ID
#     content = request.form.get('content')
#     parent_comment_id = request.form.get('parent_comment_id')
#     if parent_comment_id:
#         parent_comment = IssueComment.query.get(parent_comment_id)
#         comment = IssueComment(issue=issue, user_id=user_id, content=content, parent_comment=parent_comment)
#     else:
#         comment = IssueComment(issue=issue, user_id=user_id, content=content)    
#     db.session.add(comment)
#     db.session.commit()

#     return redirect(url_for('core.issue', issue_id=issue_id))


# @core.route('/discussions')
# def list_discussions():
#     discussions = Discussion.query.all()
#     return render_template('discussions.html', discussions=discussions)

# @core.route('/discussion/<int:discussion_id>')
# def view_discussion(discussion_id):
#     total_likes = get_total_likes(Discussion, discussion_id)
#     total_dislikes = get_total_dislikes(Discussion, discussion_id)
#     print(total_likes)
#     print("total_likes")
#     discussion = Discussion.query.get(discussion_id)
#     discussion.views = int(discussion.views) +1
#     discussion.likes = total_likes
#     discussion.dislikes = total_dislikes
#     db.session.commit()
#     discussions = Discussion.query.all()
#     polls= Poll.query.all()
#     comments = DiscussionComment.query.filter_by(discussion_id=discussion_id, parent_comment_id=None).all()
    
#     return render_template('portal/discussion.html', discussion=discussion, comments=comments,discussions=discussions,polls=polls,total_likes=total_likes,total_dislikes=total_dislikes)



# @core.route('/discussions/new', methods=['GET', 'POST'])
# def new_discussion():
#     organizations = Organization.query.all()
#     if request.method == 'POST':
#         title = request.form.get('title')
#         content = request.form.get('content')
#         discussion = Discussion(title=title, content=content, organization_id=request.form.get('organization'),user_id="1")
#         db.session.add(discussion)
#         db.session.commit()
#         return redirect(url_for('core.dashboard'))
#     return render_template('portal/newdiscussion.html',organizations=organizations)




# @core.route('/discussions/<int:discussion_id>/edit', methods=['GET', 'POST'])
# def edit_discussion(discussion_id):
#     discussion = Discussion.query.get(discussion_id)
#     if request.method == 'POST':
#         discussion.title = request.form.get('title')
#         discussion.content = request.form.get('content')
#         db.session.commit()
#         return redirect(url_for('list_discussions'))
#     return render_template('edit_discussion.html', discussion=discussion)

# @core.route('/discussions/<int:discussion_id>/delete', methods=['POST'])
# def delete_discussion(discussion_id):
#     discussion = Discussion.query.get(discussion_id)
#     db.session.delete(discussion)
#     db.session.commit()
#     return redirect(url_for('list_discussions'))

# # CRUD routes for discussion comments

# @core.route('/discussions/<int:discussion_id>/add_comment', methods=['POST'])
# def add_discussion_comment(discussion_id):
#     discussion = Discussion.query.get(discussion_id)
#     user_id = 1  # Replace with the actual user ID
#     content = request.form.get('content')
#     parent_comment_id = request.form.get('parent_comment_id')
#     print(parent_comment_id)

#     if parent_comment_id:
#         parent_comment = DiscussionComment.query.get(parent_comment_id)
#         comment = DiscussionComment(discussion=discussion, user_id=user_id, content=content, parent_comment=parent_comment)
#     else:
#         comment = DiscussionComment(discussion=discussion, user_id=user_id, content=content)

#     db.session.add(comment)
#     db.session.commit()

#     # return redirect(url_for('core.dashboard', discussion_id=discussion_id))
#     return redirect(url_for('core.dashboard'))



# @core.route('/organization/<int:organization_id>',methods=['GET', 'POST'])
# def organization(organization_id):
#     # form = NewsletterSubForm()
#     organization =  Organization.query.filter(Organization.id == organization_id).first()
#     organization.views =int(organization.views) + 1
#     db.session.commit()
#     title = organization.user.name
#     related = Organization.query.all()
#     return render_template('portal/organization.html',issue=issue,title=title,related=related)


# @core.route('/polls')
# def list_polls():
#     polls = Poll.query.all()
#     return render_template('polls.html', polls=polls)

# @core.route('/polls/<int:poll_id>')
# def view_poll(poll_id):
#     poll = Poll.query.get(poll_id)
#     print('poll')
#     print(poll)
#     options = PollOption.query.filter_by(poll_id=poll_id).all()
#     discussions = Discussion.query.all()
#     polls = Poll.query.all()
#     return render_template('portal/poll.html', poll=poll, options=options,discussions = discussions,polls=polls)

# @core.route('/polls/add', methods=['GET', 'POST'])
# def add_poll():
#     if request.method == 'POST':
#         question = request.form.get('question')
#         option_texts = request.form.get('option_text')

#         poll = Poll(question=question)
#         db.session.add(poll)
#         db.session.commit()

#         for option_text in option_texts.split(','):
#             option = PollOption(poll=poll, option_text=option_text,user_id=session['id'])
#             db.session.add(option)

#         db.session.commit()
#         return redirect(url_for('core.dashboard'))

#     return render_template('portal/newpoll.html')

# @core.route('/polls/<int:poll_id>/vote/<int:option_id>')
# def vote_poll(poll_id, option_id):
#     user_id = session['id']  # Replace with the actual user ID

#     vote = PollVote.query.filter_by(user_id=user_id, poll_id=poll_id).first()
#     if vote:
#         vote.option_id = option_id
#     else:
#         vote = PollVote(user_id=user_id, poll_id=poll_id, option_id=option_id)
#         db.session.add(vote)

#     db.session.commit()

#     return redirect(url_for('core.dashboard', poll_id=poll_id))

# @core.route('/favorite/<type>/<int:id>')
# def favorite(type, id):
#     print('favoriting')
#     user_id = session['id']  
#     if type =="discussion":
#         print("favoriting discussion")
#         iffavorite = Favorite.query.filter_by(user_id=session['id'], discussion_id=id).first()
#         if iffavorite:
#             db.session.delete(iffavorite)
#         else:
#             favorite = Favorite(user_id=user_id, likeable_id=id, likeable_type=type,discussion_id=id)
#             db.session.add(favorite)
#     elif type == "poll":
#         print("favoriting poll")
#         iffavorite = Favorite.query.filter_by(user_id=session['id'], poll_id=id).first()
#         if iffavorite:
#             db.session.delete(iffavorite)
#         else:
#             favorite = Favorite(user_id=user_id, likeable_id=id, likeable_type=type,poll_id=id)
#             db.session.add(favorite)
#     elif type == "issue":
#         print("favoriting issue")
#         iffavorite = Favorite.query.filter_by(user_id=session['id'], issue_id=id).first()
#         if iffavorite:
#             db.session.delete(iffavorite)
#         else:
#             favorite = Favorite(user_id=user_id, likeable_id=id, likeable_type=type,issue_id=id)
#             db.session.add(favorite)
#     elif type == "organization":
#         print("favoriting organization")
#         iffavorite = Favorite.query.filter_by(user_id=session['id'], organization_id=id).first()
#         if iffavorite:
#             db.session.delete(iffavorite)
#         else:
#             favorite = Favorite(user_id=user_id, likeable_id=id, likeable_type=type,organization_id=id)
#             db.session.add(favorite)
#     db.session.commit()
#     return redirect(url_for('core.dashboard'))


# @core.route('/myfavorites')
# def myfavorites():
#     favorites = Favorite.query.all()
#     myfavoriteissues = Favorite.query.filter_by(user_id=session['id'],likeable_type="issue").all()
#     myfavoritepolls = Favorite.query.filter_by(user_id=session['id'],likeable_type="poll").all()
#     myfavoritediscussions = Favorite.query.filter_by(user_id=session['id'],likeable_type="discussion").all()
#     print("myfavoriteissues")
#     print(myfavoriteissues)
#     return render_template('portal/myfavorites.html', favorites=favorites,myfavoritediscussions=myfavoritediscussions,myfavoriteissues=myfavoriteissues,myfavoritepolls=myfavoritepolls)


# # @core.route('/discussions/<int:discussion_id>/vote/<int:option_id>')
# # def vote_discussion(discussion_id, option_id):
# #     user_id = 2  # Replace with the actual user ID

# #     vote = Discussion.query.filter_by(user_id=user_id, discussion_id=discussion_id).first()
# #     if vote:
# #         vote.option_id = option_id
# #     else:
# #         vote = discussionVote(user_id=user_id, discussion_id=discussion_id, option_id=option_id)
# #         db.session.add(vote)

# #     db.session.commit()

# #     return redirect(url_for('core.dashboard', discussion_id=discussion_id))


# def create_like(user_id, likeable_id, likeable_type):
#     like = LikeDislike(user_id=user_id, likeable_id=likeable_id, likeable_type=likeable_type,value=1)
#     db.session.add(like)
#     db.session.commit()

# def create_dislike(user_id, likeable_id, likeable_type):
#     like = LikeDislike(user_id=user_id, likeable_id=likeable_id, likeable_type=likeable_type,value=0)
#     db.session.add(like)
#     db.session.commit()

# def get_total_likes(likeable_model, likeable_id):
#     return LikeDislike.query.filter_by(likeable_type=likeable_model.__name__.lower(), likeable_id=likeable_id,value=1).count()

# def get_total_dislikes(likeable_model, likeable_id):
#     return LikeDislike.query.filter_by(likeable_type=likeable_model.__name__.lower(), likeable_id=likeable_id,value=0).count()


# @core.route('/like/issue/<int:issue_id>', methods=['POST'])
# @login_required
# def like_issue(issue_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=issue_id).first()
#     if iflike:
#         if iflike.value == 1:
#             iflike.value = 0
#             print('Disliked now')
#         else:
#             print('ALREADY LIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=issue_id, likeable_type='issue',value=1,issue_id=issue_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Issue, issue_id)
#     total_dislikes = get_total_dislikes(Issue, issue_id)
#     issue = issue.query.filter_by(id=issue_id).first()
#     issue.likes = total_likes
#     issue.dislikes = total_dislikes
#     db.session.commit()
#     return redirect(url_for('core.dashboard'))

# @core.route('/dislike/issue/<int:issue_id>', methods=['POST'])
# @login_required
# def dislike_issue(issue_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=issue_id).first()
#     if iflike:
#         if iflike.value == 1:
#             iflike.value = 0
#             print('disliked now')
#         else:
#             print('ALREADY DISLIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=issue_id, likeable_type='issue',value=0,issue_id=issue_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Issue, issue_id)
#     total_dislikes = get_total_dislikes(Issue, issue_id)
#     issue = issue.query.filter_by(id=issue_id).first()
#     issue.likes = total_likes
#     issue.dislikes = total_dislikes
#     db.session.commit()
#     return redirect(url_for('core.dashboard'))

# @core.route('/like/poll/<int:poll_id>', methods=['POST'])
# @login_required
# def like_poll(poll_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=poll_id).first()
#     if iflike:
#         if iflike.value == 0:
#             iflike.value = 1
#             print('liked now')
#         else:
#             print('ALREADY LIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=poll_id, likeable_type='poll',value=1,poll_id=poll_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Poll, poll_id)
#     total_dislikes = get_total_dislikes(Poll, poll_id)
#     poll = poll.query.filter_by(id=poll_id).first()
#     poll.likes = total_likes
#     poll.dislikes = total_dislikes
#     db.session.commit()
#     return redirect(url_for('polls.view_poll', poll_id=poll_id))

# @core.route('/dislike/poll/<int:poll_id>', methods=['POST'])
# @login_required
# def dislike_poll(poll_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=poll_id).first()
#     if iflike:
#         if iflike.value == 1:
#             iflike.value = 0
#             print('Disliked now')
#         else:
#             print('ALREADY DISLIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=poll_id, likeable_type='poll',value=0,poll_id=poll_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Poll, poll_id)
#     total_dislikes = get_total_dislikes(Poll, poll_id)
#     poll = poll.query.filter_by(id=poll_id).first()
#     poll.likes = total_likes
#     poll.dislikes = total_dislikes
#     db.session.commit()
#     return redirect(url_for('core.dashboard', poll_id=poll_id))

# @core.route('/like/discussion/<int:discussion_id>', methods=['POST','GET'])
# @login_required
# def like_discussion(discussion_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=discussion_id).first()
#     if iflike:
#         if iflike.value == 0:
#             iflike.value = 1
#             print('Liked now')
#         else:
#             print('ALREADY LIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=discussion_id, likeable_type='discussion',value=1,discussion_id=discussion_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Discussion, discussion_id)
#     total_dislikes = get_total_dislikes(Discussion, discussion_id)
#     discussion = Discussion.query.filter_by(id=discussion_id).first()
#     discussion.likes = total_likes
#     discussion.dislikes = total_dislikes
#     db.session.commit()

#     return redirect(url_for('core.dashboard', discussion_id=discussion_id))

# @core.route('/dislike/discussion/<int:discussion_id>', methods=['POST','GET'])
# @login_required
# def dislike_discussion(discussion_id):
#     iflike = LikeDislike.query.filter_by(user_id=session['id'], likeable_id=discussion_id).first()
#     if iflike:
#         if iflike.value == 1:
#             iflike.value = 0
#             print('Disliked now')
#         else:
#             print('ALREADY DISLIKED')
#     else:
#         like = LikeDislike(user_id=session['id'], likeable_id=discussion_id, likeable_type='discussion',value=0,discussion_id=discussion_id)
#         db.session.add(like)
#     total_likes = get_total_likes(Discussion, discussion_id)
#     total_dislikes = get_total_dislikes(Discussion, discussion_id)
#     discussion = Discussion.query.filter_by(id=discussion_id).first()
#     discussion.likes = total_likes
#     discussion.dislikes = total_dislikes
#     db.session.commit()
#     return redirect(url_for('core.dashboard', discussion_id=discussion_id))

# # @core.route('/dislike/discussion/<int:discussion_id>', methods=['POST','GET'])
# # @login_required
# # def dislike_discussion(discussion_id):
# #     like = LikeDislike(user_id=session['id'], likeable_id=discussion_id, likeable_type='discussion',value=0,discussion_id=discussion_id)
# #     db.session.add(like)
# #     db.session.commit()
# #     return redirect(url_for('core.dashboard', discussion_id=discussion_id))

# # @core.route('/food', methods=['POST'])
# # def food():
# #     # Get the uploaded file
# #     image = request.files['file']
# #     # Save the image temporarily
# #     image_path = 'temp.png'
# #     image.save(image_path)
# #     # Use pytesseract to extract text
# #     extracted_text = pytesseract.image_to_string(Image.open(image_path))
# #     print(extracted_text)

# #     # Now, you can process the extracted_text and store it in your database

# #     # Clean up: delete the temporary image
# #     os.remove(image_path)

# #     return render_template('result.html', text=extracted_text)


# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# @core.route("/meu", methods=['GET', 'POST'])
# # @login_required
# def menu():
#     form = AboutForm()
#     if request.method =='POST':
# # Open the manipulated image
#         img = request.files.get('images')
#         # pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'venv', 'Scripts', 'tesseract.exe')
#         # filename = secure_filename(img.filename)
#                 # file.save(photos.config['UPLOADED_PHOTOS_DEST'] + '/' + filename)
#         image_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], img.filename)
#         # return img.filename
#         img.save(image_path)
#         print(image_path)

#         img_byte_array = BytesIO()
#         # img.save(img_byte_array, format='PNG')
#         img_base64 = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')
#         base64_image = encode_image(image_path)
#         # Send the image to the ChatGPT API
#         api_url = 'https://api.openai.com/v1/chat/completions'
#         api_key = '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'
#         headers = {
#             'Authorization': f'Bearer {api_key}',
#             'Content-Type': 'application/json'
#         }
#         payload = {
#             "model": "gpt-4-vision-preview",
#             "messages": [
#                 {
#                     "role": "system",
#                     "content": [
#                         {
#                             "type": "text",
#                             "text": "Extract all menu items, categories, and prices as a list ."
#                         },
#                         {
#                             "type": "image_url",
#                             "image_url": {
#                                 "url": f"data:image/jpeg;base64,{base64_image}"
#                                 # "url": "https://images.twinkl.co.uk/tw1n/image/private/t_630_eco/image_repo/4f/a5/au-t-2577-cafe-menus-australia_ver_2.jpg"

#                             }
#                         }
#                     ]
#                 }
#             ],
#             "max_tokens": 300
#         }

#         response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#         response_data = response.json()

#         if 'error' in response_data:
#             print(f"Error: {response_data['error']}")
        
#         # Parse the ChatGPT API response
#         menu_items = []

#         for message in response_data['choices'][0]['message']['content'].split('\n'):
#             # Assuming each line in the response contains an item, category, and price separated by commas
#             item_data = message.split(',')
#             menu_items.append(item_data)
#             print(item_data)

#         return render_template('menu.html', menu_items=menu_items)

#         # Use a more informative prompt
#         # prompt = 'Extract all menu items, categories, and prices from the menu image.'

#         # data = {
#         #     'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}],
#         #     'file': img_base64,
#         #     'prompt': prompt,
#         #     'model': 'text-davinci-003'
#         # }

#         # response = requests.post(api_url, json=data, headers=headers)
#         # response_data = response.json()
#         # if 'error' in response_data:
#         #     print(f"Error: {response_data['error']}")
#         # print(response)
#         # keys = response_data.keys()
#         # print(keys)

#         # # Parse the ChatGPT API response
#         # menu_items = []

#         # for message in response_data['choices'][0]['message']['content'].split('\n'):
#         #     # Assuming each line in the response contains an item, category, and price separated by commas
#         #     item_data = message.split(',')
#         #     menu_items.append(item_data)
#         #     print(item_data)
#         # return(menu_items)
#     return render_template('menu.html', form=form)

# @app.route("/menu2", methods=['GET', 'POST'])
# def menu2():
#     form = AboutForm()
#     if request.method == 'POST':
#         img = request.files.get('images')
#         image_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], img.filename)
#         img.save(image_path)

#         # Encode the image to base64
#         base64_image = encode_image(image_path)

#         # Send the image to the GPT-4 Vision API
#         api_url = 'https://api.openai.com/v1/chat/completions'
#         headers = {
#             'Authorization': f'Bearer {"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"}',
#             'Content-Type': 'application/json'
#         }

#         payload = {
#             "model": "gpt-4-vision-preview",
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": [
#                         {
#                             "type": "text",
#                             "text": "Extract all menu items, categories, and prices as a list .Eg Food Name, Price, Category/Type"
#                         },
#                         {
#                             "type": "image_url",
#                             "image_url": {
#                                 "url": f"data:image/jpeg;base64,{base64_image}"
#                             }
#                         }
#                     ]
#                 }
#             ],
#             "max_tokens": 300
#         }

#         response = requests.post(api_url, headers=headers, json=payload)
#         response_data = response.json()

#         if 'error' in response_data:
#             print(f"Error: {response_data['error']}")
        
#         # Parse the GPT-4 Vision API response
#         menu_items = response_data.get('choices', [])
#         print(menu_items)
#         # # Parse the ChatGPT API response
#         menu_items = []

#         for message in response_data['choices'][0]['message']['content'].split('\n'):
#             # Assuming each line in the response contains an item, category, and price separated by commas
#             item_data = message.split(',')
#             menu_items.append(item_data)
#             print(item_data)
#         # return(menu_items)
#         return render_template('menu.html', menu_items=menu_items)

#     return render_template('menu.html', form=form)
