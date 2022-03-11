from tkinter.messagebox import askServiceretrycancel
from urllib import response
#neded to download nltk for language processing
#import nltk
#nltk.download('punkt')
#nltk.download()
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def conversation_start():
    #tokenize to make a list for easy access to iterate through
    phrase = word_tokenize(input(f"Would you like to review a product or a service?\n"))
  
    ps = PorterStemmer()
    while True:
        #to determine if the user mentions product, service, neither, or both in the response
        mentionProduct = False
        mentionService = False
        
        for p in phrase:
            if ps.stem(p) == "product":
                mentionProduct = True
            #note: when using stem on services the program breaks it down to "servic" instead of serivce
            if ps.stem(p) == "servic":
                mentionService = True
        
        #if only product is mentioned
        if mentionProduct == True and mentionService == False:
            product_start()
        #if only service is mentioned
        elif mentionProduct == False and mentionService == True:
            service_start()
        #if both or neither are mentioned, clarify if they want a product or service first
        else:
            phrase = word_tokenize(input(f"Please clarify if you would like to review a product or service first by typing either product or service\n"))

def service_start():
    ps = PorterStemmer()
    service = word_tokenize(input(f"""Which of our services would you like to discuss?
           massages
           hair cuts
           pedicures\n"""))
    while True:
    
        # to determine which of the options have been mentioned in response
        mentionMassage = False
        mentionHair = False
        mentionPedicure = False
        for s in service:
            #note: when using stem on massage the program breaks it down to "massag"
            if ps.stem(s) == "massag":
                mentionMassage = True
            if ps.stem(s) == "hair":
                mentionHair = True
            #note: when using stem on predicure the program breaks it down to "pedicur"
            if ps.stem(s) == "pedicur":
                mentionPedicure = True

        #if only 1 of the serivces is mentioned, go to that specifically. If not, redo 
        if mentionMassage == True and mentionHair == False and mentionPedicure == False:
            reviewService("massage")
        elif mentionMassage == True and mentionHair == False and mentionPedicure == False:
            reviewService("hair cut")
        elif mentionMassage == True and mentionHair == False and mentionPedicure == False:
            reviewService("predicure")
        else:
            service = word_tokenize(input(f"""Please specify which service you would like to review first:
               massages
               hair cuts
               pedicures\n"""))

def reviewService(serviceName):
    #needs number input
    review = input(f"How would you rate your {serviceName}? (0-10)\n")
    if review > 7:
        positiveService(serviceName)
    elif review <=7:
        negativeMassage(serviceName)

def positiveService(serviceName):
    askServiceReview = input(f"sounds like you had a great time your {serviceName}, would you be willing to give us a review on how we did?\n")
    while True:
        if askServiceReview.lower() == 'yes':
            deepServiceReview()
        elif askServiceReview.lower() == 'no':
            print("Thank you for your rating\n")
            discuss_Another()
        else:
            askServiceReview = input(f"Didn't quite get that. Can you please indicate yes or no?\n")

def negativeMassage(serviceName):
    askServiceReview = input(f"sounds like you had a poor time with your {serviceName}, would you be willing to give us a review on how we did?\n")
    while True:
        if askServiceReview.lower() == 'yes':
            deepServiceReview(serviceName)
        elif askServiceReview.lower() == 'no':
            print("Thank you for your feedback\n")
            discuss_Another()
        else:
            askServiceReview = input(f"Didn't quite get that. Can you please indicate yes or no?\n")


def deepServiceReview(serviceName):
    askService = word_tokenize(input(f"Do you remember who gave you your {serviceName}?\n"))
    ps = PorterStemmer()
    
    #go through phrase to see if they "dont" remember or they do 
    #note: use of don't breaks the porter stemmer algorithmn into "do" and "n't"
    dontInstance = False
    rememberInstance = False
    
    for a in askService:
        #checks for dont and no
        if ps.stem(a) == 'dont' or ps.stem(a) == 'no':
            dontInstance = True
        #checks for do and yes
        if ps.stem(a) == 'do' or ps.stem(a) == 'yes':
            rememberInstance = True

    #checks if they remember or not
    if dontInstance == True and rememberInstance == False:
        rememberReview()
    elif dontInstance == False and rememberInstance == True:
        forgetReview(serviceName)
    else:  
        askService = word_tokenize(input(f"Didn't quite catch that, can you please indicate if you remember who gave you your {serviceName}?\n"))

def rememberReview():
    name = input(f"what was their name?\n")
    recommend = input(f"would you recommend {name} to another person?\n")
    goodPoint = input(f"what did we do well with?\n")
    feedback = input(f"how can we do better?\n")

    print("""Your review has been saved!
    would you recommend {name}: {recommend}
    what did we do well: {goodPoint}
    how can we do better: {feedback}""")
    discuss_Another()

def forgetReview(serviceName):
    recommend = input(f"would you recommend {serviceName} to another person?\n")
    goodPoint = input(f"what did we do well with?\n")
    feedback = input(f"how can we do better?\n")
    
    print("""Your review has been saved!
    would you recommend {name}: {recommend}
    what did we do well: {goodPoint}
    how can we do better: {feedback}""")
    discuss_Another()

def product_start():
    repeat = True
    while repeat == True:
        product = input(f"Which product would you like to discuss?\n")
        initial_conversation(product)
        
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
        # askService if they are happy with their purchase
        elif question.lower() == "no":
            negative_feedback(question)            
            break
        else:
            question = input("Didn't quite get that. Can you please indicate yes or no?\n")

def discuss_Another():
    reviewNextProduct = input(f"Would you like to discuss another product or service?\n")
    while True:
        if reviewNextProduct.lower() == 'yes':
            conversation_start()
        elif reviewNextProduct.lower() == 'no':
            print ("Thank you for your time")
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
    print('Do you have an receipt?\n')
    hasOrderNo = input()
    if hasOrderNo.lower() == 'yes':
        print('Please enter your receipt number.\n')
        orderNo = input()
        print('Alright, we will send you an email with the next steps.\n')
    elif hasOrderNo.lower() == 'no':
        print('Ok. What is the email adress you used to place your order?\n')
        email = input()
        print('Alright, we will send you an email with the next steps.\n')
    else:
        print("Didn't quite get that. Can you please indicate yes or no?\n")
        refund(product)
    discuss_Another()

def negative_feedback(product):
    ## If customer is unsatisfied with product
    while True:
        # If they are not happy with their purchase
        # askService if they want a refund
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
               
        # askService if they want to review the product
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

        
conversation_start()


