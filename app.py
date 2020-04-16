# Import our pymongo library, which lets us connect our Flask app to our Mongo database
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 


# Create an instance of our Flask app.
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape_app")

# Set route
@app.route('/')
def home():
    #Find a record
    mars_facts = mongo.db.collection.find_one()

    # Return the template and data
    return render_template('index.html', mars=mars_facts)

@app.route('/scrape')
def scrape():
    mars_facts_data = scrape_mars.scrape()
    
    #Update Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_facts_data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)