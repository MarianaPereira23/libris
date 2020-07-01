# [LIBRIS](https://libris-project.herokuapp.com/)

Libris, meaning books in Latin, is a book review website designed for users to make reviews on books they already have read or find their next book to read from other users reviews.

## UX

### Strategy Plane

Being Libris a book review website the UX can be divided in people who have read a book and what to review it, people who are looking for a new book to read and the website owner.

* As a reader that finished a book I expect to be able to find or add the book I read and be able to add a comment to it's page in order to share my thoughts about it.
* As a reader looking for a new book to read I expect to find books sorted by genre and to have not only a small description of each book, but also some reviews from other readers.
* As the site owner I expect that this website will turn profitable by providing an affiliate "Buy me" link for each book.

### Scope Plane

Considering the User Stories in the Strategy Plane it is important that the website has the following:
* A set of books with the book cover, author, description, date of publishing and genre;
* The possibility to add new books and edit or delete existing ones (in case of error or duplication for example);
* The possibility to comment the existing books to give them a review and a rating;
* A way to sort through books based on author or genre;
* Display of the book average rating from the user ratings (while there is no rating to a book, nothing should appear).

### Structure Plane

In terms of structure we can divide my work as follows: 
1. Base html file - Contains the header and the footer to be used in all pages;
2. Homepage - Contains a nice black and white book picture, a phrase related to reading from a known personality, book suggestions to the users and a list with all the book genres available that also act as a link that takes the user to a automatic search books by the clicked genre;
3. Books and search results pages - Both pages have the same structure and they show all the books present in the database (or all the books that correspond to the search). The books are separated by a solid border and every books shows its title on top, then a cover picture on the left and the book information on the right. Also, when clicking on the book title the user is taken to the page of that book;
4. Book page - Like in the previous page here you have the book title on top, then a cover picture on the left and the book information on the right. The user will also have, contrary to what happens on the pages from 3. The ability to edit that books information or even completely delete the book. After this comes a section with user reviews where people can review the book and delete existing reviews;
5. Add and edit book pages - A simple page with a form with all the necessary fields to add a new book to the database or to edit an existing book (in this last case, the fields come pre-filled and the user only needs to change what is wrong;
6. Community page - A sort of user forum where people can share tips or insights (here the posts form and display will have a similar structure as the reviews from book page;
7. Contact page - Accessible only through the footer, since the goal of this website is not to be contacted, but I felt the option should exist nonetheless. In this page the user will find a rendered map with the location of the office (fictitious) and a contact form to reach the team (form not connected on purpose).

### Skeleton Plane & Surface Plane

The following wireframes are good representative of these two planes, since most of the design decisions were made when making the wireframes.

* [Homepage for Desktop](static/wireframes/HomepageDesktop.jpg)
* [Homepage for Mobile](static/wireframes/HomepageMobile.jpg)
* [Posts and Books page for Desktop](static/wireframes/BooksDesktop.jpg)
* [Posts and Books page for Mobile](static/wireframes/BooksMobile.jpg)

### Database Schema

My database collection on MongoDB is organized according to the following:

1. books
    1. _id (automatically given by MongoDB)
    2. book_title
    3. cover_photo
    4. author
    5. year
    6. synopsis
    7. collection
    8. genre
2. books_comments - connected to books through the book_title
    1. _id (automatically given by MongoDB)
    2. book_title
    3. username
    4. comment
    5. rating
3. posts - independent
    1. _id (automatically given by MongoDB)
    2. username
    3. post

## Features

### Existing Features

* Search field where users can search by book title or book author;
* Search by genre implemented on genre list in homepage;
* Ability to add new books to website;
* Ability to edit existing books;
* Ability to make a review on a book;
* Ability to delete an existing review;
* Book rating automatically calculated from user ratings average;
* Ability to make a post in the community section/discussion;
* Ability to delete a post;
* Navbar in all pages made using Bootstrap;
* Review and posts form hidden behind button using JavaScript;
* Leaflet map that shows (fictitious) address for the company in the Contact page.

### Features Left to Implement

* Link to buy book;
* Possibility to also search by collection name;
* Non-static book suggestions (get book suggestions from top rated books);
* User sign up and loggin;
* Make it impossible for users to delete reviews or posts that are not their own;
* Instead of letting users immediatelly add, edit or delete books, I would like them to fill the forms as are now, but instead of going directly to the database, making the info go to site management team as a request (to prevent users from deleting everything on website for example).

## Technologies Used

* HTML
* CSS
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Bootstap](https://getbootstrap.com/)
    + The project uses Bootstrap to simplify html, css and JavaScript coding.
* [FontAwesome](https://fontawesome.com/)
    + The project uses FontAwesome to put pictograms on the map markers and on the description of the places
* [GoogleFonts](https://fonts.google.com/)
    + The project uses GoogleFonts as the font supplier for the website
* [JQuery](https://jquery.com/)
    + The project uses JQuery to simplify DOM manipulation
* [MongoDB](https://www.mongodb.com/)
    + The project uses a MongoDB database to store all relevant information, such as books, reviews and posts
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* PyMongo
    + The project uses PyMongo as the Python API for MongoDB
* [Leaflet API](https://leafletjs.com/) and [OpenSteetMap](https://www.openstreetmap.org/#map=15/10.3714/-85.1239)
    + The project uses the Leaflet API together with OpenStreetMap to render the map in the regional pages.
* Git
    + The project used Git for version control, commits were submited as often as possible


## Testing

The website was tested for the following:

1.	Homepage loads correctly
2.	Links in navbar and homepage for search by genre work accordingly and display only corresponding matches – Read functionality 
3.	Link to see all displays every book on database – Read functionality
4.	Input to search by author or book title displays matches when existing and a message when no match exists – Read functionality
5.	Add book link on navbar works correctly and loads wanted page
6.	Form to add book is not sent if required fields are not filled (marked with an *) and a message appears asking the user to fill those fields.
7.	Also in add book form, the URL and year fields should also display a message if the URL is not correctly formatted and the year is not numeric
8.	When correctly filled the add book form adds a new entry to the database – Create functionality
9.	Going back to browsing all books, by genre or even by book title or author displays the new book – Read functionality
10.	When browsing all books or search results clicking on a book title redirects the user to that books page – Read functionality
11.	In the book page the edit book button takes the user to a form similar to the add book form, with the exception that all fields that have information are pre-filled and the user only needs to add new information or correct existing information – Update functionality
12.	Going back to search for that book shows the new updated information – Read functionality
13.	In the book page the delete button displays a modal confirming the user wishes to delete, if the user clicks cancel the book is not deleted and if the user clicks delete the book is removed from the database – Delete functionality
14.	After deleting the book, it does not display anywhere in the website or database anymore
15.	Back to a specific book page, bellow all the book information and the buttons that refer to the book there is a review section where the user can add a book review. The add review form, similarly to the other forms already discussed, also has required fields that without being filled will prevent the form from being sent – Create functionality 
16.	After sending the form the user is kept in the same page and the review that was just added is displayed on top of the reviews section – Read functionality
17.	All reviews display a delete button that works just like the book delete button – Delete functionality 
18.	When a book has reviews, a numeric rating should be displayed on the top right corner of the book section of the page with an average of the reviews rating, and when no review exists yet said number should not be displayed
19.	Adding a review will change the book rating automatically
20.	Same goes for deleting a review. And deleting all reviews will cause the book rating to not be displayed at all, since it does not exist.
21.	In the community page users are able to write general posts – Create functionality
22.	The added posts are displayed (from most recent to oldest) beneath the option to create a new post – Read functionality
23.	All posts possess a delete button that works in the same way as the previous delete buttons – Delete functionality
24.	The contact page, only accessible through the footer since the goal of this website is not to be contacted – displays a leaflet map with the location of the offices
25.	Also in the contact page there is a form to contact the team that when filled and sent displays a modal with a thank you message, however, unlike the other forms, this form is not connected on the back-end of the project since no email for this website was created to receive the messages
26.	Finally, in the footer, the social media links take the user to their homepage and not to the “Libris” page, since that page was also not created.

Apart from the tests listed above, all buttons, link and the carousel buttons were tested in several devices to make sure they work appropriately.
Besides myself I also got 5 more people testing all the things listed above to make sure no errors were found.

Finally, the website was thoroughly tested to make sure it displays properly in different devices and brands (Apple, Xiaomi, Samsung, Hp, Huawei, Acer), with different screen sizes (from Iphone, to tablet, to windows pc and Imac) and different browsers (Chrome, Safari, Mozilla and Opera).

### Code Validation

* [W3C HTML Validator tool](https://validator.w3.org/) was used to validate all HTML code;
* [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/) was used to validate all CSS code;
* [JSHint](https://jshint.com/) was used to validade JavaScript syntax;
* [Pep8 Online tool](http://pep8online.com) was used to validate Python syntax.

## Deployment

This project is hosted by Heroku and the deployed site should update immediately in case there is any change to the master branch. 
The deployment was made following these steps:

1. Login to Heroku in their webpage and create app
2. Type heroku login in the terminal and login
3. Type heroku apps in the terminal to confirm that the app you created in step 1 is listed
4. Go back to your app page in Heroku, copy the heroku command to create a new Git repository and paste that command in your terminal
5. If you don't already have a requirements.txt file, create one by typing pip3 freeze -- local > requirements.txt in your terminal and add it to Git
6. Create a Procfile by typing echo web: python app.py > Procfile (in case the file that is the entry point to your app is a Python file named app.py) and add it to Git
7. Push to Heroku using the command git push heroku master
8. Type heroku ps:scale web=1 in your terminal to get the application running on Heroku
9. Go back over to your application in Heroku's webpage, go to settings, click on Reveal Config Vars and specify your Ip (0.0.0.0), Port (5000) and any environment variables or secret keys or app might need
10. Oppen the app (top right corner of your app's Heroku page) and you are done

In case you wish to clone this repository, follow these steps:

1. Go to the GitHub page for the repository you wish to clone
2. Click the green button that says “Clone or Download”
3. Copy the URL given in the Clone with HTTPS
4. Open your repository and its terminal
5. Type git clone and then paste the URL you got on step 3
6. Press Enter
7. Create database in MongoDB
8. Create collections for the database
9. Add your Mongo URI in a file that should be listed as a .gitignore
10. Install all requirements by typing in the terminal pip3 install -r requirements.txt and you are done!

## Credits

### Content

Since this is a website purely for educational purposes the synopsis of the books was copied from their page in [Goodreads](https://www.goodreads.com/). All the remaining content was fully written by me.

### Media

Image that can be found on homepage was taken from [Unsplash](https://unsplash.com/). 
The cover photos for the books were taken from their page in [Wikipedia](https://www.wikipedia.org/). 