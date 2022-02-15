def conversation():
    repeat = True
    while repeat == True:
        product = input(f"Which product would you like to review?\n")
        mv_skeleton_convo(product)
        repeat = review_Another()
def mv_skeleton_convo(product):
    # Initial Prompt
    question = input(f"Would you like to review {product}?\n")
    while True:
        # If user input is 'yes'
        # Go through the review process then break
        
        if question.lower() == "yes":
            rating = input(f"Great! How many stars would you rate the {product}? (0 - 10)\n")
            recommend = input(f"Would you recommend {product} item to a friend?\n")
            purchaseDate = input(f"When did you purchase the {product}?\n")
            
            print(f"""Your review has been saved!
            Rating: {rating}
            Would you recommend: {recommend}
            Date of Pruchase: {purchaseDate}
            """)
            break
        
        # If user input is 'no'
        # Ask if they are happy with their purchase
        elif question.lower() == "no":
            while True:
                decision = input(f"Okay. Are you happy with this purchase?\n")
                
                # If they are happy with their purchase, break
                if decision.lower() == "yes":
                    print("Okay! Have a good day!")
                    break
                
                # If they are not happy with their purchase
                # Ask if they want a refund
                elif decision.lower() == "no":
                    refund = input("That's too bad. Would you like a refund?\n")
                    while True:
                        
                        # If they want a refund, email will be sent. Break
                        if refund.lower() == "yes":
                            print("Okay, we'll send you an email shortly to begin the process")
                            break
                        
                        # If they want don't want a refund, break
                        elif refund.lower() == "no":
                            print("Okay, have a good day!")
                            break
                        else: 
                            refund = input("Didn't quite get that. Can you please indicate yes or no?\n")
                    break
                else:
                    decision = input("Didn't quite get that. Can you please indicate yes or no?\n")
            
            break
        else:
            question = input("Didn't quite get that. Can you please indicate yes or no?\n")
def review_Another():
    reviewNextProduct = input(f"Would you like to review another product?")
    while True:
        if reviewNextProduct.lower() == 'yes':
            return True
        elif reviewNextProduct.lower() == 'no':
            print ("Thank you for your time")
            return False
        else: 
            reviewNextProduct = input(f"Didn't quite get that. Can you please indicate yes or no?\n")   
conversation()

