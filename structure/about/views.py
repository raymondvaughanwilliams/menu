# from PIL import Image
# import requests
# from io import BytesIO
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# from flask import render_template,url_for,flash,redirect,request,Blueprint,session
# from werkzeug.utils import secure_filename
# from structure import db,mail ,photos
# import secrets
# from structure.about.forms import AboutForm


# about = Blueprint('about',__name__)

# @about.route("/menu", methods=['GET', 'POST'])
# # @login_required
# def menu():
#     form = AboutForm()
#     if request.method =='POST':
# # Open the manipulated image
#         img = request.files.getlist('images')

#             # Process and save each uploaded file to the database
#             # for img in uploaded_files:
#             #     # if img:
#         filename = secure_filename(img.filename)
#         print(filename)
#                 # file.save(photos.config['UPLOADED_PHOTOS_DEST'] + '/' + filename)
#         image = photos.save(img, name=secrets.token_hex(10) + ".")
#         image= "static/uploads/issues/"+image

#                 # Save file details to the database and associate with the issue
#                 # upload = Upload(filename=image, issue=issue, issue_id=issue.id)
#                 # db.session.add(upload)
#                 # db.session.commit()
#         # image_path = 'path/to/manipulated/image.png'
#         img = Image.open(image)

#         # Convert the image to bytes
#         img_byte_array = BytesIO()
#         img.save(img_byte_array, format='PNG')

#         # Send the image to the ChatGPT API
#         api_url = 'https://api.openai.com/v1/chat/completions'
#         api_key = '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'
#         headers = {
#             'Authorization': f'Bearer {api_key}',
#             'Content-Type': 'application/json'
#         }

#         # Use a more informative prompt
#         prompt = 'Extract all menu items, categories, and prices from the menu image.'

#         data = {
#             'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}],
#             'file': img_byte_array.getvalue(),
#             'prompt': prompt
#         }

#         response = requests.post(api_url, json=data, headers=headers)
#         response_data = response.json()

#         # Parse the ChatGPT API response
#         menu_items = []

#         for message in response_data['choices'][0]['message']['content'].split('\n'):
#             # Assuming each line in the response contains an item, category, and price separated by commas
#             item_data = message.split(',')
#             menu_items.append(item_data)
#             print(item_data)
#         return(menu_items)
#     return render_template('menu.html', form=form)
   

    

# # # Save menu items to the database
# # for menu_item in menu_items:
# #     db.session.add(menu_item)

# # db.session.commit()
