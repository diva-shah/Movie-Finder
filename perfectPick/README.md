github username: pythonqueen7
project name: Perfect Pick

INTRODUCTION AND CREDITS

Perfect Pick is an application where users can find movies like they can on Amazon Prime Video. Moreover, when the user first opens the application, they must register themself, however if they user is already registered, they must log in. 

For the register, logoutLink, loginForm functions, I basically copied the code from project4 because there is only just one way to complete these functions and since I was not required to do these tasks before, I was clueless on how to complete them.

Moreover, my layout.html is copied from project4 (except for some minor changes) because the navigation bar from that project was exactly what I was going for and since it was previously completed for me as it was given code in the distribution code, I was not sure how to go about writing it. 

I also got help from the Discord community and the internet for bugs I wasn't sure how to fix as well as minor pieces of code (such as django sql queries).

I also frequently referenced my previous projects to see how I solved certain issues and then came up with ideas on how to solve my issue
FUNCTIONS OF EACH FILE

Once the user logs in or registers, they are taken to the index page which displays movies given from the first page of data from TMDB API and also shows a search bar where the user can type in anything and they will get searches for movies that match the search string; if no movie matches the search request, a text is displayed saying that there are no movies that match the user's request.

Also, if the user scrolls far down enough, my application loads the next page of movies from the TMDB API from my load function (I copied the code from lecture 6 for writing the if condition of when to call my load function)

If the user clicks on any movie, they are taken to a page where they see the movie title, poster, overiew, cast, genres, rating, and runtime. The cast, genres, ratings, and runtime was given from OMDB API and the movie title, overview, and poster was given from TMDB API. This page is the movieInfo.html file in the templates/perfectPick folder.

Along with those pieces of information about the movie, the user is given the option to add the movie to their watchlist and the option to like the movie. If the user clicks on the "Add Item To Watchlist" link, they are redirected to the index page, and if they click on the movie they just added to the watchlist, the text changes to "Remove Item From Watchlist".

On the other hand, if the user clicks on the like button, they page refreshes and shows that the heart becomes white to red.

Further, on the navigation bar, there are options to click on "Perfect Pick", "Watchlist", "Liked Movies", and "Log Out". Clicking on Perfect Pick takes the user to the index page (index.html); clicking on Watchlist takes the user to a page where all the movies that the user added to their watchlist is displayed (watchlist.html); clicking on Liked Movies redirects the user to a page that shows all the movies they have liked (liked.html); and clicking on Log Out logs the user out.

Finally, in the index page, the top has a search bar with a search icon and the user can submit their query by either pressing enter or clicking on the icon. The page that displays the filtered movies is search.html.

DISTINCTIVENESS AND COMPLEXITY

My project is very distinct from other projects because I am focused on movies, and none of the other projects were based on movies. The only features that overlap with previous projects are those of the watchlist and liked movies but these are very common features to have in an application. 

Next, my project if more complex than the Pizza Project because I am using python, javascript, and json/ 2nd-party API's to make my application function. Since I am using API's I require to make fetch calls which means I had to use more advanced techniques than those used in the Pizza Project as that project did not required APIs. Also, since I was using a 2nd-party API, I had to come up with different and maybe even more creative ways to be able to add movies to the user's watchlist and liked movies list.

Moreover, in terms of corresponding features, the Menu feature of the Pizza project is similar to my index page but mine is more complex because I required getting information from an api.

Also, since the data of the movies was not mine, I had to figure out a way on accessing that information like I would if the data was mine (as in if I was adding and editting data in the json database). My solution to this was adding the movieID to a model (if it was not already in the model) everytime the user clicked on the movie for its information, added the movie to their watchlist, or liked that movie.

MOBILE RESPONSIVE

I added if conditions based on the windows inner width and the css is different if the innerWidth is less than 1440

HOW TO RUN THE PROGRAM

My program requires the python packages listed in the requirements.txt, however you must also import the specific functions that are imported in my views.py or else the program won't work and it will throw errors.

Other than that, my program should work with "python manage.py runserver" or "python3 manage.py runserver" depending on the version of your python.