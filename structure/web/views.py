import atexit
import csv
import os
from os import environ
from uuid import uuid4
import secrets
from random import randint, choice
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
from structure.web.forms import SearchForm ,AddFoodsForm
from structure.models import User  , Category , Restaurant , Food ,Comment
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract 
from io import BytesIO
import base64
from faker import Faker

web = Blueprint('web', __name__)
fake = Faker()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@web.route("/food/imageadd", methods=['GET', 'POST'])
def imageadd():
    api_key = os.environ.get('API_KEY')
    form = AboutForm()
    form2 = AddFoodsForm()
    categories = Category.query.all()
    restaurants = Restaurant.query.all()
    if request.method == 'POST':
        img = request.files.get('images')
        image_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], img.filename)
        img.save(image_path)

        # Encode the image to base64
        base64_image = encode_image(image_path)

        # Send the image to the GPT-4 Vision API
        api_url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Extract all menu items, categories, and prices as a list .Eg Food Name, Price, Category/Type"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post(api_url, headers=headers, json=payload)
        response_data = response.json()
        # response_data = 

        if 'error' in response_data:
            print(f"Error: {response_data['error']}")
        
        # Parse the GPT-4 Vision API response
        menu_items = response_data.get('choices', [])
        print(menu_items)
        # # Parse the ChatGPT API response
        menu_items = []

        for message in response_data['choices'][0]['message']['content'].split('\n'):
            # Assuming each line in the response contains an item, category, and price separated by commas
            item_data = message.split(',')
            menu_items.append(item_data)
            print(item_data)
        # return(menu_items)
        return render_template('web/addfood2.html', menu_items=menu_items,form =form2, categories =categories ,restaurants =restaurants)

    return render_template('web/addfood2.html', form=form)



@web.route('/index')
def index():
    form = SearchForm()
    per_page = 40
    page = request.args.get('page', default=1, type=int)
    restaurants_query = Restaurant.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('web/index.html', restaurants=restaurants_query,form=form)

@web.route('/restaurants')
def restaurants():
    per_page = 40
    page = request.args.get('page', default=1, type=int)
    restaurants_query = Restaurant.query.all()
    return render_template('web/restaurants.html', restaurants=restaurants_query)

@web.route('/restaurant/<int:id>')
def restaurant(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    foods = Food.query.filter_by(restaurant_id=id).all()

    return render_template('web/restaurant.html', restaurant=restaurant,foods=foods)

@web.route('/filters', methods=['GET', 'POST'])
def filter_page():
    form = SearchForm(request.form)

    if request.method == 'POST':
        # Build the query based on the form inputs
        query = Restaurant.query.join(Food)
        print(form.food_name.data)
        print(form.restaurant_name.data)
        if form.food_name.data:
            query = query.filter(Food.name.ilike(f"%{form.food_name.data}%"))

        if form.restaurant_name.data:
            query = query.filter(Restaurant.name.ilike(f"%{form.restaurant_name.data}%"))

        if form.min_price.data is not None:
            query = query.filter(Food.price >= form.min_price.data)

        if form.max_price.data is not None:
            query = query.filter(Food.price <= form.max_price.data)

        restaurants = query.all()
    else:
        # If no form submission, show all restaurants
        restaurants = Restaurant.query.all()
    
    print(restaurants)

    return render_template('web/filter.html', form=form, restaurants=restaurants)

@web.route('/search',methods=['GET', 'POST'])
def search():
    form = SearchForm()
    filtered = "no"
    if request.method=="POST":
        filtered = "yes"
        print(request.form.get('type') )
        if request.form.get('type') == "food":
            
            food = request.form.get('text')
            # Build the SQLAlchemy filter conditions
            conditions = []
            if food:
                # Build a list of conditions that match the location field
                # using the LIKE operator and the % wildcard
                food_conditions = [
                    Food.name.like(f"%{food}%"),
                    Food.name.like(f"{food}%"),
                    Food.name.like(f"%{food}"),
                ]
                # Use the OR operator to combine the conditions into a single
                # condition that matches any of the location variations
                conditions.append(or_(*food_conditions))
                # conditions.append(or_(Delivery.start_date.between(date_min, date_max),Delivery.end_date.between(date_min, date_max)))
            print(conditions[0])
            foods = Food.query.filter(and_(*conditions)).all()
            print(foods)
            return render_template("web/foodfilter.html", foods=foods,form=form ,filtered=filtered)
        elif request.form.get('type') == "restaurant":
            print("searching...")
            # Get the filter values from the form
            restaurant = Restaurant.query.all()
            text = request.form.get('text')
            print(text)
            # # Build the SQLAlchemy filter conditions
            conditions = []
            if restaurant:
                restaurants =Restaurant.query.filter(Restaurant.name.like(f"%{text}%")).all()
                # Build a list of conditions that match the location field
                # using the LIKE operator and the % wildcard
            #     restaurant_conditions = [
            #         Restaurant.name.like(f"%{text}%")
            #     ]
            #     # Use the OR operator to combine the conditions into a single
            #     # condition that matches any of the restaurant variations
            #     conditions.append(or_(*restaurant_conditions))
            # restaurants = Restaurant.query.filter(and_(*conditions)).all()
            print("restaurants")
            print(restaurants)
            return render_template("web/filter.html",form=form,restaurants=restaurants, filtered = filtered)


@web.route('/filter',methods=['GET', 'POST'])
def filter():
    form = SearchForm()
    restaurant = Restaurant.query.all()
    # destinations = Destination.query.all()
    # user =User.query.filter_by(id=session['id'])
    if request.method == "POST":
        print("searching...")
        # Get the filter values from the form
        text = form.restaurant_name.data
        # # Build the SQLAlchemy filter conditions
        conditions = []
        if restaurant:
            # Build a list of conditions that match the location field
            # using the LIKE operator and the % wildcard
            location_conditions = [
                Restaurant.name.like(f"%{text}%")
            ]
            # Use the OR operator to combine the conditions into a single
            # condition that matches any of the location variations
            conditions.append(or_(*location_conditions))
        restaurants = Restaurant.query.filter(and_(*conditions)).all()
        return render_template("web/filter.html",form=form,restaurants=restaurants)

    return render_template('web/filter.html',form=form)

@web.route('/foodfilter',methods=['GET', 'POST'])
def foodfilter():
    filterform = SearchForm()
    # foods = Food.query.all()
    filtered = "no"
    if request.method == "POST":
        print("searching...")
        # Get the filter values from the form
        filtered = "yes"
        food = filterform.food_name.data
        price_min = filterform.min_price.data
        price_max = filterform.max_price.data
        # Build the SQLAlchemy filter conditions
        conditions = []
        if food:
            # Build a list of conditions that match the location field
            # using the LIKE operator and the % wildcard
            food_conditions = [
                Food.name.like(f"%{food}%"),
                Food.name.like(f"{food}%"),
                Food.name.like(f"%{food}"),
            ]
            # Use the OR operator to combine the conditions into a single
            # condition that matches any of the location variations
            conditions.append(or_(*food_conditions))
        if price_min and price_max:
            # Filter for Deliverys with dates within the specified range
            # conditions.append(and_(Delivery.start_date >= date_min, Delivery.end_date <= date_max))
            conditions.append(and_(Food.price <= price_max,Food.price >= price_min))
            # conditions.append(or_(Delivery.start_date.between(date_min, date_max),Delivery.end_date.between(date_min, date_max)))
        print(conditions[0])
        foods = Food.query.filter(and_(*conditions)).all()
        print(foods)
        return render_template("web/foodfilter.html", foods=foods,form=filterform ,filtered=filtered)

    return render_template('web/foodfilter.html',form=filterform,filtered=filtered)


@web.route('/restaurant/add', methods=['GET', 'POST'])
def new_restaurant():
    form= SearchForm()
    categories = Category.query.all()
    restaurants = Restaurant.query.all()
    if request.method == 'POST':
        
        # print(form.restaurants.entries)


                # Create Food object and add to the database
        restaurant = Restaurant(
                    name=request.form.get('name'),
                    bio=request.form.get('bio'),
                    location=request.form.get('location'),
                    contact1=request.form.get('contact1'),
                    contact2=request.form.get('contact2'),
                    contact3=request.form.get('contact3'),

                )
        db.session.add(restaurant)

        db.session.commit()
    return render_template('web/addrestaurant.html',categories=categories , restaurants=restaurants,form=form)




@web.route('/food/add', methods=['GET', 'POST'])
def new_food():
    form = AddFoodsForm()
    categories = Category.query.all()
    restaurants = Restaurant.query.all()
    if request.method == 'POST':
        print(request.form)
        restaurant_id = request.form.get('restaurant')
        print(restaurant_id)
        print("restaurant_id")
        # print(form.foods.entries)

        for i in range(len(form.foods.entries)):
            # Retrieve values from the form
            food_name = request.form.get(f'name-{i}', '')  # Provide a default value if the field is not found
            food_price = request.form.get(f'price-{i}', '')
            food_category_id = int(request.form.get(f'foods-{i}-category', 0))  # Provide a default value if the field is not found

            # Check if all required fields are filled in
            if food_name and food_price and food_category_id:
                # Create Food object and add to the database
                food = Food(
                    name=food_name,
                    price=food_price,
                    category_id=food_category_id,
                    restaurant_id=restaurant_id
                )
                db.session.add(food)

        db.session.commit()
    return render_template('web/addfood.html',categories=categories , restaurants=restaurants,form=form)



@web.route('/submit_menu', methods=['POST'])
def submit_menu():
    if request.method == 'POST':
        foods = request.form.getlist('food_name')
        prices = request.form.getlist('food_price')
        categories = request.form.getlist('foods-category')
        restaurant = request.form.get('restaurant')

        # Assuming foods, prices, and categories have the same length
        for food_name, price, category_id in zip(foods, prices, categories):
            # Create Food object and add to the database
            food = Food(
                name=food_name,
                price=price,
                category_id=category_id,
                restaurant_id = restaurant
                # Add other fields as needed
            )
            db.session.add(food)

        db.session.commit()

        return redirect(url_for('web.index'))  # Redirect to a success page or any other route

    return render_template('error.html')


        # food = Food(name=request.form.get('name'), category_id = request.form.get('category') , restaurant_id=request.form.get('restaurant'),price = request.form.get('price'))
        # db.session.add(food)
        # db.session.commit()
        # return redirect(url_for('web.new_food'))
    # return render_template('web/addfood.html',categories=categories , restaurants=restaurants,form=form)



@web.route('/restaurant/<int:restaurant_id>/add_comment', methods=['POST'])
def add_comment(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    content = request.form.get('content')
    parent_comment_id = request.form.get('parent_comment_id')
    if parent_comment_id:
        parent_comment = Comment.query.get(parent_comment_id)
        comment = Comment(restaurant=restaurant,  content=content)
    else:
        comment = Comment(restaurant=restaurant,  content=content)    
    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('web.restaurant', restaurant_id=restaurant_id))




@web.route('/faker')
def generate_dummy_data():
    # Create dummy categories
    for _ in range(5):
        category = Category(name=fake.word())
        db.session.add(category)

    db.session.commit()

    # Create dummy restaurants
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.company(),
            bio=fake.text(),
            location=fake.address(),
            contact1=fake.phone_number(),
            contact2=fake.phone_number(),
            contact3=fake.phone_number(),
            image1=fake.image_url(),
            image2=fake.image_url(),
            image3=fake.image_url(),
            views=randint(1, 100),
            date=fake.date_between(start_date='-1y', end_date='today')
        )
        db.session.add(restaurant)

    db.session.commit()

    # Create dummy foods
    for _ in range(20):
        food = Food(
            name=fake.word(),
            price=randint(5, 50),
            category_id=choice(Category.query.all()).id
        )
        db.session.add(food)

    db.session.commit()