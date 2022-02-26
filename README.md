# COSC310 Team1 Chatbot
## Project Description
The purpose of this project is to create a customer service chat bot agent which will communicate with basic canned sentences. The chat bot will offer the opportunity for users to leave reviews or return specific products from its online store. This conversation between the user and chat bot is “smooth,” and provides the user with a realistic customer service conversation which can undergo 30 or more turns of dialogue. 

To develop this software, our team decided to work with the Agile Scrum SDLC. The rationale behind choosing Scrum is because we wanted to follow a model that allows the flexibility to monitor the software development as the project is being developed throughout the term. Utilizing Scrum will allow the team to provide feedback throughout any stage of the project and iterate accordingly.

## Running the Chatbot
The chatbot currently works through the command line. Future versions will include a UI and enable users to use the chatbot without downloading.

Either download this repository or clone it to your desired directory with 
```git clone https://github.com/mvallido/cosc310_team1_chatbot``` 
in the command line

Once you have navigated to the ```cosc310_team1_chatbot``` directory with the command line, run the python file with the ```python mv_skeleton.py``` command.

## Class Descriptions
### Opening Conversation
- Prompts the user with ```Which product would you like to discuss?```
- The user can respond with any product name
### Initial Conversation
- Asks the user if they are satisfied with the product
- User provides a yes or no answer
- If the user does not provide a yes or no answer, the bot responds with ```Didn't quite get that. Can you please indicate yes or no?```
### Positive Feedback
- If the user likes the product, the bot will ask if the user if they would like to leave a review
- User provides a yes or no answer
- If the user does not provide a yes or no answer, the bot responds with ```Didn't quite get that. Can you please indicate yes or no?```
### Write Review
- If the user would like to leave a review, the following prompts are displayed in succession:
  * ```What is your name?```
  * ```How many stars would you rate the {product}?```
  * ```Would you recommend {product} item to a friend?```
  * ```When did you purchase the {product}?```
- After these questions are anweres, the bot will display the review:
```
  Your review has been saved!
    Name: {name}
    Rating: {rating}
    Would you recommend: {recommend}
    Date of Pruchase: {purchaseDate}
```
### Deep Review
- After the user has written a review, they are asked if they would like to provide a comment for the product
- User provides a yes or no answer
- If the user does not provide a yes or no answer, the bot responds with ```Didn't quite get that. Can you please indicate yes or no?```
- If the user would like to leave a comment, they are prompted with ```Please provide your comment on {product}``` 
### Discuss Another
- After leaving a review, the user will be asked if they would like to discuss another product
- User provides a yes or no answer
- If the user does not provide a yes or no answer, the bot responds with ```Didn't quite get that. Can you please indicate yes or no?```
- If yes, the bot calls the ```opening_conversation``` function and goes through the cycle again
- If no, then the conversation is over

### Negative Feedback
- User is prompted with ```That's too bad. Would you like a refund?```
- User provides a yes or no answer
- If the user does not provide a yes or no answer, the bot responds with ```Didn't quite get that. Can you please indicate yes or no?```
- If yes, the ```refund``` function is called then breaks
- If no, the user is immediately asked ```Would you like to review the product?```
- If yes, call ```write_review``` function then break
- If no, then break
### Refund
- If the user would like a refund for the product, they are prompted with the following questions:
  * ```Do you have an order number```
  * ```Please enter your order number```
  * If the user has their order number:
    * ```What is the reason for your return?```
    * ```Alright, we will send you an email with the next steps.```
  * If the user does not have their order number:
    * ```Ok. What is the email adress you used to place your order?```
    * ```What is the reason for your return?```
    * ```Alright, we will send you an email with the next steps.```
