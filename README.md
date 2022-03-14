# COSC310 Team1 Chatbot
## Project Description
The purpose of this project is to create a customer service chat bot agent which will communicate with basic canned sentences. The chat bot will offer the opportunity for users to leave reviews or return specific products from its online store. This conversation between the user and chat bot is “smooth,” and provides the user with a realistic customer service conversation which can undergo 30 or more turns of dialogue. 

To develop this software, our team decided to work with the Agile Scrum SDLC. The rationale behind choosing Scrum is because we wanted to follow a model that allows the flexibility to monitor the software development as the project is being developed throughout the term. Utilizing Scrum will allow the team to provide feedback throughout any stage of the project and iterate accordingly.

## Installation and Running the Chat Bot
The chatbot currently works through the command line. Future versions will include a UI and enable users to use the chatbot without downloading.

Either download this repository or clone it to your desired directory with 
```git clone https://github.com/mvallido/cosc310_team1_chatbot``` 
in the command line

### Install PyTorch and NLTK (A3)
For PyTorch Installation, follow this [link](https://pytorch.org/get-started/locally/)

For NLTK, run the following commands in your CLI:
```pip install nltk```

If you get an error trying to run the program, run the following:
```$ python
>>> import nltk.download('all')
```

### Running Bot
First, run:
```python train.py```

Then, run app.py to start the chat bot:
```python app.py```

## Conversation Flow (A3)
![image](https://user-images.githubusercontent.com/61817636/158088234-0a9e4185-52a1-454f-b4da-4a337ee09f65.png)

## Coversation Structure

```
"tag": "service_review_received",
"patterns": [
          All of the user inputs which can be classified under the tag
        ],
        "responses": [
          All the responses which the bot can choose from
          ]
      }
```
### Opening Conversation
```
"tag": "greeting",
"patterns": [
          "Hi",
          "Hey",
          "How are you",
          "Is anyone there?",
          "Hello",
          "Good day"
        ],
        "responses": [
          "Hello, would you like to discuss a product or a service?",
          "Hi there, would you like to discuss a product or a service?"
        ]
```
### Product Conversation
```
"tag": "product_initial",
"patterns": [
          "Discuss a product please",
          "I'd like to discuss a Product",
          "I would like to discuss a product",
          "Can we discuss a Product",
          "Discuss"
        ],
        "responses": [
          "Sounds good! Would you like to leave a review or receive a refund on your most recently purchased product?",
          "Okay. Would you like to leave a review or receive a refund for the last product you purchased?"
        ]
```
### Product Review
```
"tag": "product_review",
"patterns": [
          "I would like to leave a Product review please",
          "Product review",
          "Can I leave a product review",
          "Can I review a product"
        ],
        "responses": [
          "Sounds good. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars",
          "Okay. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars",
          "Will do. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars"
        ]
```
### Product Received
```
"tag": "product_review_received",
"patterns": [
          "Product Review 0",
          "Product Review 1",
          "Product Review 2",
          "Product Review 3",
          "Product Review 4",
          "Product Review 5",
          "Product Review"
        ],
        "responses": [
          "Thank you for your review! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time",
          "Your review has been saved! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time",
          "We have received your review! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time"
        ]
```
## Product Refund
```
"tag": "product_refund",
"patterns": [
          "I would like to a refund please",
          "Can I get a refund",
          "refund"
        ],
        "responses": [
          "Sounds good. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Okay. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Will do. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?"
        ]
```
## Service Conversation
```
"tag": "service_initial",
"patterns": [
          "Service please",
          "I'd like to review a service",
          "Can I review a service",
          "Service review"
        ],
        "responses": [
          "Sounds good! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures",
          "Okay! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures",
          "Will do! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures"
        ]
```
## Service Review
```
"tag": "service_review",
"patterns": [
          "I would like to leave a review for the massage please",
          "I would like to leave a review for the haircut please",
          "I would like to leave a review for the pedicure please",
          "Massage",
          "Haircuts",
          "Pedicures",
          "Can I leave a massage review",
          "Can I leave a haircut review",
          "Can I leave a pedicure review"
        ],
        "responses": [
          "Sounds good. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars",
          "Okay. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars",
          "Will do. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars"
        ]
```
## Service Review Received
```
"tag": "service_review_received",
"patterns": [
          "Service Review 0",
          "Service Review 1",
          "Service Review 2",
          "Service Review 3",
          "Service Review 4",
          "Service Review 5",
          "Service Review"
        ],
        "responses": [
          "Thank you for your review! If you liked their service, you can specify you want Mary for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Your review has been saved! If you liked their service, you can specify you want James for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "We have received your review! If you liked their service, you can specify you want John for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?"
        ]
      }
```
## New Features (A3)
- GUI:
  * Implemented a GUI with Tkinter for better user experience 
- PyTorch and NLTK:
  * We implemented this toolkits to improve spelling mistakes and enable the chatbot to have more than one common response to similar user inputs
- Extra Topic:
  * In addition to the product review, we now offer services and the ability to review them as well 
 
### Sample output with user typos
![image](https://user-images.githubusercontent.com/61817636/158089817-452c73b5-2784-42f7-bb00-f37168f8d502.png)

## References (A3)
To implement the GUI, PyTorch, and NLTK the following resources were used to implement all features:
- [Contextual Chatbots with Tensorflow](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077?gi=f7d03c3a78c3)
- [Chat bot with PyTorch, NLP, and Deep Learning](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg&ab_channel=PythonEngineer)
- [GUI with Tkinter](https://www.youtube.com/watch?v=RNEcewpVZUQ)
