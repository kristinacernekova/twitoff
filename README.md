# twitoff

Build a Flask web application to predict, between two Twitter users, who is more likely to post a given Tweet
Build a SpaCy model that predict most probable user (from a pool) of a given tweet
Deploy the model to Heroku so that predictions can be displayed to the user

# Web Application Development with Flask
In the modern day, most applications we interact with are web applications - client-server architectures delivered via HTTP and accessed with a web browser.
Create a simple Python web application that exposes an API to URL endpoints.
Flask is not as fully featured as a development framework as other Python web development frameworks (like Django for example). However, its simplicity lets us build an app by writing code that is closer to vanilla Python. Because the framework's doing less work for us, there's less about how the framework works that we'll have to learn.

# Consuming Data from an API
A data-backed application is only as good as the data it has - and a great way to get a lot of data is through an API. The idea of an API is actually very general, but in the modern day usually refers to "asking some other service to give you (some of) their data." A lot of apps are built this way, especially when starting out, but there are some steps and hoops to get it working.
Connect to the Twitter API and query for tweets by various parameters
Implement a SpaCy NLP model to create embeddings from our tweet text.
Check out Tweepy, a Python package that facilitates accessing the Twitter API.
Explore the SpaCy, you can use the word2vect to fitpredictive models such as regression to numerical data. This allows us to work with things data scientist like most - digits - opposed to unstructured words. These numbers are referred to as "embeddings" - the numbers representing the words or phrases from the vocabulary.

# Adding Data Science to a Web Application
We have a basic working web application, and one that pulls real data (Tweets and their embeddings), now we add some data science. We're going to fit a predictive model based on Tweet embeddings and allow the client to use the model to make predictions of which user is more likely to tweet given text.
Run and report simple online analysis of data from the user or an API.
Run a more complicated offline model, and serialize the results for online use.
We already have all needed dependencies and accounts.

# Web Application Deployment
We have a web application going, but it's not really on the web yet. Linking to a GitHub repo and linking to a live working application reaches a broader audience. Anybody, whether they are technical or not, can click and enjoy!
Deploy a basic (single-server) web application to common cloud services.
Securely connect a deployed web application to a relational database back-end.
Use free Heroku account and deploy.

