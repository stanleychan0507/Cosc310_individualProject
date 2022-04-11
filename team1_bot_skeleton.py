from urllib import response
import wikipedia
import googlemaps
import pprint
import time

def opening_conversation():
    repeat = True
    while repeat == True:
        product = input(f"Do you want to discuss a product or see different location on the site?\n")
        if product.lower() == "discuss a product":
            product = input(f"Which product would you like to discuss?\n")
            wikipedia_api(product)
        elif product.lower() == "see different location":
            googleplace_api(product)
        
def initial_conversation(product):
    # Initial Prompt
    question = input(f"Are you satisfied with {product}?\n")
    while True:
        # If user input is 'yes'
        # Go through the review process then break
        
        if question.lower() == "yes":
            positive_feedback(product)
            break
        
        # If user input is 'no'
        # Ask if they are happy with their purchase
        elif question.lower() == "no":
            negative_feedback(question)            
            break
        else:
            question = input("Didn't quite get that. Can you please indicate yes or no?\n")

def discuss_Another():
    reviewNextProduct = input(f"Would you like to discuss another product?")
    while True:
        if reviewNextProduct.lower() == 'yes':
            opening_conversation()
            break
        elif reviewNextProduct.lower() == 'no':
            seeSiteLocation = input(f"Do you want to see our the different location on our sites?")
            if seeSiteLocation.lower() == 'yes':
                googleplace_api()
            elif seeSiteLocation.lower() == 'no':
                print("Thank you for your time!")
                quit()
        else: 
            reviewNextProduct = input(f"Didn't quite get that. Can you please indicate yes or no?\n")   
        break
    
def positive_feedback(product):
    ## If customer is satisfied with product
    while True:
        review = input(f"Great! Would you like to review the {product}?\n")
        while True:
            if review.lower() == "no":
                discuss_Another()
                break
            elif review.lower() == "yes":
                write_review(product)
                break
            else:
                review = input("Didn't quite get that. Can you please indicate yes or no?\n")
        break
    
def refund(product):
    print('Do you have an order number?\n')
    hasOrderNo = input()
    if hasOrderNo.lower() == 'yes':
        print('Please enter your order number.\n')
        orderNo = input()
        reason = input('What is the reason for your return?\n')
        print('Alright, we will send you an email with the next steps.\n')
    elif hasOrderNo.lower() == 'no':
        print('Ok. What is the email adress you used to place your order?\n')
        email = input()
        reason = input('What is the reason for your return?\n')
        print('Alright, we will send you an email with the next steps.\n')
    else:
        print("Didn't quite get that. Can you please indicate yes or no?\n")
        refund(product)
    discuss_Another()

def negative_feedback(product):
    ## If customer is unsatisfied with product
    while True:
        # If they are not happy with their purchase
        # Ask if they want a refund
        refundInput = input("That's too bad. Would you like a refund?\n")
        while True:
                # If they want a refund, email will be sent. Break
                if refundInput.lower() == "yes":
                    refund(product)
                    break

                # If they want don't want a refund, break
                elif refundInput.lower() == "no":
                    break
                else: 
                    refundInput = input("Didn't quite get that. Can you please indicate yes or no?\n")
               
        # Ask if they want to review the product
        review = input("Would you like to review the product?\n")
        while True:
            if review.lower() == "no":          
                discuss_Another()
            elif review.lower() == "yes":
                write_review(product)
            else:
                review = input("Didn't quite get that. Can you please indicate yes or no?\n")

def write_review(product):
    name = input(f"What is your name? \n")
    rating = input(f"How many stars would you rate the {product}? (0 - 10)\n")
    recommend = input(f"Would you recommend {product} item to a friend?\n")
    purchaseDate = input(f"When did you purchase the {product}?\n")
    
    print(f"""Your review has been saved!
    Name: {name}
    Rating: {rating}
    Would you recommend: {recommend}
    Date of Pruchase: {purchaseDate}
    """)
    deep_review(product)

def deep_review(product):
    deepReview = input(f"Would you like to provide a comment on {product}?\n")
    while True:
        if deepReview.lower() == 'yes':
            detailedReview = input(f"Please provide your comment on {product}\n")
            print(f"""Your comment has been saved!\n
            Comment: {detailedReview}""")
            break
        elif deepReview.lower() == 'no':
            break
        else: 
            deepReview = input(f"Didn't quite get that. Can you please indicate yes or no?\n")
        discuss_Another()              

def wikipedia_api(product):
    print("Here are some information about your product :")
    print(wikipedia.search(product))
    initial_conversation(product)

def googleplace_api(product):
    print("Here are the different site around campus site :")
    gmaps = googlemaps.Client(key = "AIzaSyCVm2ijkKshgMCpIhL8t1JksRPyRgJo8a4")
    places_result = gmaps.places_nearby(location='49.940403, -119.395492', radius = 100, open_now = False, type = 'university')
    for place in places_result['results']:
        my_place_id = place['place_id']
        my_fields = ['name', 'formatted_phone_number', 'type']
        place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
        print(place_details)
        break
    opening_conversation(product)

opening_conversation()