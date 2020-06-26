# LIBRIS

Libris, meaning books in Latin, is a book review website designed to users can make reviews on books they already have read or find their next book from other users reviews.

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
* The possibility to comment the existing books to give them a review;
* A way to sort through books based on author or genre;
* The possibility to click a link and go directly to the store to buy said book.

### Structure Plane

In terms of structure we can divide my work as follows: 
1. Base html file - Contains the header and the footer to be used in all pages;
2. Homepage - Contains a nice black and white book picture, a phrase related to reading from a known personality, book suggestions to the users and a list with all the book genres available that also act as a link that takes the user to a automatic search books by the clicked genre;
3. Books and search results pages - Both pages have the same structure and they show all the books present in the database (or all the books that correspond to the search). The books are separated by a solid border and every books shows its title on top, then a cover picture on the left and the book information on the right. Also, when clicking on the book title the user is taken to the page of that book;
4. Book page - Like in the previous page here you have the book title on top, then a cover picture on the left and the book information on the right. The user will also have, contrary to what happens on the pages from 3. The ability to edit that books information or even completely delete the book. After this comes a section with user reviews where people can review the book and delete existing reviews;
5. Add and edit book pages - A simple page with a form with all the necessary fields to add a new book to the database or to edit an existing book (in this last case, the fields come pre-filled and the user only needs to change what is wrong;
6. Community page - A sort of user forum where people can share tips or insights (here the posts form and display will have a similar structure as the reviews from book page.

### Skeleton Plane

* [Homepage for Desktop](static/wireframes/HomepageDesktop.jpg)
* [Homepage for Mobile](static/wireframes/HomepageMobile.jpg)
* [Posts and Books page for Desktop](static/wireframes/BooksDesktop.jpg)
* [Posts and Books page for Mobile](static/wireframes/BooksMobile.jpg)

### Surface Plane

The links present in the footer icons actually take the user to the homepage of each social media since I didn't really create a social media page for my website.

## Features

### Existing Features

### Features Left to Implement

## Technologies Used

## Testing

## Deployment

## Credits

### Content

Since this is a website purely for educational purposes the synopsis of the books was copied from their page in Goodreads.

### Media

The cover photos for the books where taken from their page in Wikipedia.

### Acknowledgements