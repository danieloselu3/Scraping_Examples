# imports
import requests

# the base urlfor accessing the API
base_url = "https://hacker-news.firebaseio.com/v0"

# set an empty list to old the data
articles = []

# create a link to get the topstories ids
top_stories = requests.get(base_url + "/topstories.json").json()

# loop through the top 3 topstories id
for id in top_stories[:3]:
    story_link = base_url + '/item/' + str(id) + '.json'
    story = requests.get(story_link).json()

    # send the retrieved data up to the articles list
    articles.append(story)

print('{} stories where found.'.format(len(articles)))
print("--------")
print("Here are the top 3")
print("--------")
for article in articles:
    print(article)
    print("")


# NOTE : There are 400+ stories in the top stories, 
# combined with the multiple concatenations in the 
# formation of the links (line 11 and 15) this makes 
# the script load slow, and thats why we've looped 
# over only 3 items in line 14.