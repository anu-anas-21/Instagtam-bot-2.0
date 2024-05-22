from time import perf_counter
from instapy import InstaPy

#Login Section
session = InstaPy(username="username", password="password", headless_browser=True)
session.login()

#Like Section
session.like_by_tags(["javascript","python"],amount=6)

#Follow Section
session.set_do_follow(True, percentage=25)

#Comment Section
session.set_do_comment(True, percentage=50)
session.set_comments(["Sun kissed" , "Lovely" , "Keep it up"])

session.end()
