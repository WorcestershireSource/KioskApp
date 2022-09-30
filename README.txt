
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



Useful links:
Sign into Square Developer dashboard: https://developer.squareup.com/
Bootstrap documentation: https://getbootstrap.com/docs/5.2/getting-started/introduction/

