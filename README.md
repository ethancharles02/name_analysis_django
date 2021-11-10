# Overview

### Name Analysis
Inspiration for this project came from one of my data science classes from a while back. We analyzed name data and made graphs for it.

I thought that was really interesting so I decided to move it over to Django as my first Django project.

On the request page, type in a name to get data on that name.

You can also type in a state abbreviation to get data specifically from that state. If nothing is typed in, it will just give data for all the states.

### Video
[Software Demo Video](https://youtu.be/4avzIqrN4Kk)

# Web Pages

I made 3 main web pages with 1 extra page just in case the user types in something that doesn't work.

The main page doesn't have any specific Django syntax other than a connection to a render function.

The request page has a Django form so that the user can send their input to the Python code.

The data page shows the graphs that are produced and has if statements in the template just in case the urls aren't available.

# Development Environment

This project was made using VS Code and Django

# Useful Websites

* [VS Code Django Guide](https://code.visualstudio.com/docs/python/tutorial-django)
* [Django Documentation](https://docs.djangoproject.com/en/3.2/)

# Future Work

* Move requests over to SQL
* Add more HTML and CSS for formatting to make it look nicer
* Add more customizable graph options than just state and total numbers