from datetime import date

# importing the random module
import random


# import Flask ::: for implementig flask server
from flask import Flask, render_template,request


# create a new web-app whixh is a Flask application while __name__	represents that his is  
#the file that will reresent the web-app		
app = Flask(__name__,static_url_path='/static')

#import .jason files => hotels.json
import json
with open('quotes.json') as data_file1:    
		data1 = json.load(data_file1)
		quote = data1['quotes'] # gor a list 

#GLOBAL-variables => check_in, check_out.


#/ represent the default page llocalhost/
@app.route("/")
#Declarator funtion
def index():
	today = date.today() 
	rand = random.randint(0,102)
	print(quote[rand])
	print(quote[rand]['author'])
	return render_template("jokes.html",quote=quote[rand], rand = rand , today = today)

@app.route("/aman",methods=["get"])
def aman():
	return render_template("me.html")


if __name__ == '__main__':
	app.run()  