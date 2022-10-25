
# Kiosk Application


## Overview:
This is a web application to act as a kisok for a coffee shop. 
It relies on an API with the payment provider 'Square'.

The application is based on a HMTL/CSS and Javascript front end. It uses JQuery and Ajax for a responsive experience.
It uses a python/flask backend, which controls the communication with the payment provider: Square.

## Purpose
This app should allow a small shop to set up a self-service kiosk which will reduce the staffing resource needed to run the shop.

Existing kiosk solutions are expensive and not commonly available in smaller shops. 

## Process
The backend requests the shop's inventory from Square - this is passed to the front end and used to populate the menu that appears to the user

The customer selects their purchases - this is handled in the front end to ensure a responsive interface.
When the customer is ready to pay, the order is posted to the server and the app uses a Square API to initiate a payment with a Square 'terminal': a credit/debit card reader.
The user can pay using the square terminal - details of their payment are processed by Square and not passed through the kiosk app for security.

[![alt text](https://img.youtube.com/vi/r4SIV6AEF-Y/0.jpg)](https://www.youtube.com/watch?v=r4SIV6AEF-Y)

*Image: click on the image for a video walkthrough of the app*


## Useful commands:
- python -m flask --debug run             *Start a Flask session*
- export SQUARE_ACCESS_TOKEN=     *Include the correct token for Square to work - get it from the developer dashboard below*
- source .venv/bin/activate       *Start the virtual environment*

## Useful links:
- Sign into Square Developer dashboard: https://developer.squareup.com/
- Bootstrap documentation: https://getbootstrap.com/docs/5.2/getting-started/introduction/
- Test values for terminal payment: https://developer.squareup.com/docs/devtools/sandbox/testing 
- Square advice on taking payments with the terminal: https://developer.squareup.com/docs/terminal-api/square-terminal-payments

## Square terminal instructions:
- Pair terminal and POS application with Devices API: https://developer.squareup.com/docs/terminal-api/pos-integration
- Send checkout request with Terminal API - request to API can specify terminal behaviours https://developer.squareup.com/docs/terminal-api/square-terminal-payments

## Files used
Index.html - the main page of the application
App.py - the main flask app 
Squarecode.py - APIs to connect the application to the payment provider e.g. sending order details for payment
styles.css - additional CSS used where bootstrap wasn't sufficient
kioskfrontend.js - the javascript logic to manage the user experience e.g. tracking what is in the user's basket

## Learning outcomes:
I initially developed the application relying heavily on flask to track the users order, but this resulted in a slower user experience. 

To complete this project I therefore had to learn more about Javascript. I used the CS50 web development lectures and further online training including learning to use JQuery and AJax to ensure the site was responsive.

I used the bootstrap framework to ensure the application displayed correctly in full screen view.

I learned to use more of the tools in the Chrome Developer tool to debug my application and to check its appearance on different devices. 

Using the Square APIs was challenging and was the first time I'd had to follow that kind of developer documentation. Their developer dashboards and sandbox test environment provided excellent tools for testing and debugging the application. 

I made an initial mock up in Swift UI, but decided these languages would allow more flexibility in deployment hardware/tablets. 