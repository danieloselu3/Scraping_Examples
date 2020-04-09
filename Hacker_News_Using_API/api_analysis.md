The API documentation can be found at *https://github.com/HackerNews/API*

## Base url -> *https://hacker-news.firebaseio.com/v0*
    This is the url we'll use to access the api

## Top_stories url -> *https://hacker-news.firebaseio.com/v0/topstories.json*
    This is the url that will return to us all the top stories id's
    the result is a list of over 400+ ids.

We'll first get the IDs of the top stories, convert it into a json object,
store it into a variable, the loop into each item, concatenate it with the
base url.

using each link we've created, we'll access the API to extract the required data.
