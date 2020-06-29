# LIBRIS

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
6. Community page - A sort of user forum where people can share tips or insights (here the posts form and display will have a similar structure as the reviews from book page.

### Skeleton Plane & Surface Plane

The following wireframes are good representative of these two planes, since most of the design decisions were made when making the wireframes.

* [Homepage for Desktop](static/wireframes/HomepageDesktop.jpg)
* [Homepage for Mobile](static/wireframes/HomepageMobile.jpg)
* [Posts and Books page for Desktop](static/wireframes/BooksDesktop.jpg)
* [Posts and Books page for Mobile](static/wireframes/BooksMobile.jpg)

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
* Review and posts form hidden behind button using JavaScript.

### Features Left to Implement

* Link to buy book;
* Possibility to also search by collection name;
* Non-static book suggestions (get book suggestions from top rated books);
* User sign up and loggin;
* Make it impossible for users to delete reviews or posts that are not their own;
* Instead of letting users immediatelly add, edit or delete books, I would like them to fill the forms as are now, but instead of going directly to the database, making the info go to site management team as a request (to prevent users from deleting everything on website for example)

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


## Testing

Note: The links present in the footer icons actually take the user to the homepage of each social media, on purpose, since I didn't create a social media page for my website.

## Deployment

This project is hosted by Heroku and the deployed site should update immediately in case there is any change to the master branch. 
The deployment was made following these steps:

1. Login to Heroku in their webpage and create app
2. Login to Heroku in the terminal

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

Since this is a website purely for educational purposes the synopsis of the books was copied from their page in Goodreads. All the remaining content was fully written by me.

### Media

Image that can be found on homepage was taken from [Unsplash](https://unsplash.com/). 
The cover photos for the books were taken from their page in Wikipedia. 