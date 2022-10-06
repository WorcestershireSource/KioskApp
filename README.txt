
Overview:
This is a web application to act as a kisok for a coffee shop. 
It relies on an API with the payment provider 'Square' and sends commands to a robotic arm and a DEPro Espresso machine
The model is written in Python. The View is written in html/css with Bootstrap




Issues:
Unsure if app will open in full screen on an ipad - see here: : https://www.ispringsolutions.com/blog/how-to-make-a-website-full-screen-on-the-ipad   https://stackoverflow.com/questions/48774142/after-upgrade-to-ios-11-3-web-app-does-not-show-full-screen-per-apple-mobile-web
Unsure how Square Terminal will respond to commands
Unsure how to connect Square Terminal to web application
Not yet clear how I can get actual catalogue from my shop - executing code fetches nothing 
Will web application be responsive enough?

DEPro and robotic arm integrations still unknown


Useful commands:
python -m flask --debug run             Start a Flask session
export SQUARE_ACCESS_TOKEN=     Include the correct token for Square to work - get it from the developer dashboard below
source .venv/bin/activate       Start the virtual environment

export SQUARE_ACCESS_TOKEN=EAAAEMaP4K5nSYlD_YOy-2xprFeUvrwUiY4DsHdG5h34fbhA7knyifWw598ihaU5

Useful links:
Sign into Square Developer dashboard: https://developer.squareup.com/
Bootstrap documentation: https://getbootstrap.com/docs/5.2/getting-started/introduction/
Test values for terminal payment: https://developer.squareup.com/docs/devtools/sandbox/testing 









Square terminal instructions:

Pair terminal and POS application with Devices API: https://developer.squareup.com/docs/terminal-api/pos-integration
Sedn checkout request with Terminal API - request to API can specify terminal behaviours 
https://developer.squareup.com/docs/terminal-api/square-terminal-payments


Test 
https://developer.squareup.com/docs/terminal-api/square-terminal-payments
See the 'did you know' box on this page for info about testing terminal in sandbox
Recommends that you use 'webhooks' to check when payment is completed as there could be a long delay?


App must specify the total amount to be paid
1) call create device code - Says that in production you must use API and not take device ID from seller dashboard...
2) await confirmation of pair
3) send the terminal api request to check out 
4) square sends checkout details to terminal
5) buyer pays
6) square terminal notifies square of the payment
7) Terminal notifies backend that checkout was completed


Can give total amount to be charged or can pass an order ID created with the order API
    Order must belong to same location YES
    Order must be in OPEN state ???
    Currencies must match
    Order and checkout value must match
