# netflix-show-reviews

[Deployed App](https://netflix-public-review-board.herokuapp.com/)

One issue with browsing on one's netflix account is that you cannot see public reviews for the movies or shows you are considering taking time out of your life to watch. Crowdsourcing public reviews is one of the most transparent ways to indicate the suitability of a movie/show to a user. This website contains information on nearly 9000 different netflix movies and shows sourced from this [dataset on Kaggle](https://www.kaggle.com/datasets/infamouscoder/dataset-netflix-shows)

Users can login or sign up if they wish to leave a review of their own.

This is a fullstack application that uses Python and Flask for setting up the backend with the server and RESTful API routes. Movies, reviews, and user data are stored in an MySQL database with all queries configured using the SqlAlchemy ORM. THe layout and styles were built with HTML and CSS and functions for handling client side data and making fetch requests to the api were written in javaScript.
