# 100 Days Of Code - Log

### Day 0: July 31, 2019

**Today's Progress**: Preparing for the challenge, setting up git and stuff

**Thoughts**: None

**Link(s) to work**: None


### Day 1: August 1, 2019

**Today's Progress**: I've played with classes in python, ran into a few problems with inheriting from superclass, but managed to figure it out

**Thoughts**: It's easier to work with classes using python(instead of Java), no need to use @override and similar syntax.

**Link(s) to work**: https://github.com/eXTure/code-playground/blob/master/game_classes.py


### Day 2: August 2, 2019

**Today's Progress**: Today I started working with pygame library and managed to write a bit of code to display a game window, BUT I ran into problems with pylint having problems with pygame, I found something, that I need to whitelist pygame or add exceptions, but I've not managed to do that yet.

**Thoughts**: I've read that it's basically a VS Code IDE problem, maybe I should use some other IDE when working with pygame. Subllime Text maybe.

**Link(s) to work**: https://github.com/eXTure/code-playground/tree/master/Cross%20The%20Road


### Day 3: August 3, 2019

**Today's Progress**: I continued to work on the game, added basic images, but more importantly, I started applying OOP practices for this game code.

**Thoughts**: So I downloaded Atom, to work with pygame, no more problems and I like the design of it. Also I started using "Cmder", cmd alternative. It looks nicer and has git integration and I can use unix commands on it, like "ls"

**Link(s) to work**: https://github.com/eXTure/code-playground/tree/master/Cross%20The%20Road


### Day 4: August 4, 2019

**Today's Progress**: I've added keyboard controls to the game, also a background and other images, enemy functionality and border detection.

**Thoughts**: Feels nice to be able to move the character, I'm now thinking about other functionalities I could add to this mini game! Although, I'll need to add enemy collision first.

**Link(s) to work**: https://github.com/eXTure/code-playground/tree/master/Cross%20The%20Road


### Day 5: August 5, 2019

**Today's Progress**: I've finished the game together with the tutorial so no I'm gonna be implementing my own improvements to the game. What tutorial did not cover was the collision of many entities and I'm trying to figure out, how to fix this. I've tried looping on list, but something is not right.

**Thoughts**: I think next improvement should be score tracking and highscore table.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 6: August 6, 2019

**Today's Progress**: I've tried implementing a better solution for checking collision of multiple objects, but failed, so I implemented simpler solution for now. Also, I wanted to improve levels by making speed refresh to that of the first level, after additional entities appear, but I had problems with global variables, somehow it did not track the global variable. I'll have to come back to this later too.

**Thoughts**: To improve level design, I first drew out level/speed table on paper to better visualize difficulty system. This helped me a bit.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 7: August 7, 2019

**Today's Progress**: Finally I've managed to fix the correlation between level and speed. Also added logging.

**Thoughts**: The game logic now works perfectly and I can send this game to a friend to try it out! Although I have to find out, how to make python app runnable without terminal.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 8: August 8, 2019

**Today's Progress**: I've added scoring system with 2 functions: calculation of the score and writing score to the high score text file.

**Thoughts**: I think the next step is to ask what is the name of the player before the game starts, so that the scoring system make sense. And also, to add button where player could check highest score while in game

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 9: August 9, 2019

**Today's Progress**: Added the ability to enter your name before the game has started and it is later displayed in the scores. Since scores are written randomly in the text file, I decided to create a sorting algorithm to sort name by the highest score.

**Thoughts**: Reading and writing data to the txt file seems like unsafe and cumbersome choice. I'll have to check other options like excel or something.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 10: August 10, 2019

**Today's Progress**: I've added a functionality to see your score while in game, by pressing space key. Also added an informing message when a player presses left or right shift key, a message appears on the screen that you can't run faster with shift key pressed. But that could be a new functionality later.

**Thoughts**: This time I didn't had much time, but I've managed to wake up earlier than I would need, to do the challenge.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 11: August 11, 2019

**Today's Progress**: Moved images to a separate folder and spent rest of the time looking up and trying out different ways of making a dictionary from a text file in order to sort my highscores file.

**Thoughts**: Maybe I'm taking wrong approach here. Maybe dictionary is not the best choice for such task.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 12: August 12, 2019

**Today's Progress**: Finally fixed and made the sorting algorithm for sorting highscores file.

**Thoughts**: This was probably the hardest thing I did on this project yet. I wrote 73 lines of code just to sort a single file. I'm sure an experienced programmer could find a better solution, but I felt good after cracking this one.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 13: August 13, 2019

**Today's Progress**: I made it so that sorting algorithm is now automatically launched when a player looses the game and the score is counted. Also I found out, if you don't use name==main method with main() function, then, when you import the file, it's automatically launched.

**Thoughts**: That wouldn't be fine, but then the scores would be sorted before the current game score is counted. I also found out 3 ways of launching external python file.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 14: August 14, 2019

**Today's Progress**: My next aim is to display at least top three scores on screen while in game playing with a TAB key. I got down to how I would display them, but I can't get the scores yet. Since I could easily get top 3 sorted score in highscore_sorting.py file, I thought that's what I should do. But where I got stuck, is getting particular value from one python file into another. I found the solution of getting that value with import, but somehow it doesn't make it's way to the main file, I believe this might be because the file at first need to be run in order to access that particular value.

**Thoughts**: I'll figure out a way eventually.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 15: August 15, 2019

**Today's Progress**: I've managed to get that value I was trying, now the highest scores are correctly display on the screen when a player presses TAB key.

**Thoughts**: I think I'm done with this game for now, I implemented the functionalities that I thought about when I started working with this project. I'll have to start a different project, unless I'll think of other small improvements I could make. I already have other project ideas.

**Link(s) to work**: https://github.com/eXTure/Cross-The-Road


### Day 16: August 16, 2019

**Today's Progress**: Started working on scraping, having problem with getting requests.

**Thoughts**: I found one possible solutions, I'll try another day.

**Link(s) to work**: https://github.com/eXTure/code-playground


### Day 17: August 18, 2019

**Today's Progress**: I've managed to solve the request thing and scraped 2 different websites. I think I'll try to scrape something more difficult next time, since now I only tried getting contact data and similar stuff just to get started with scraping.

**Thoughts**: Would be nice to think of something useful I could scrape for myself.

**Link(s) to work**: https://github.com/eXTure/Python-Scrapes


### Day 18: August 19, 2019

**Today's Progress**: Scraped one more website and than moved on to working with flask. Prepared flask environment and initiated hello world page.

**Thoughts**: I found a good guide on flask, gonna follow it a bit since I have 0 knowledge about how to work with Flask.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask


### Day 19: August 20, 2019

**Today's Progress**: Completed base and index templates, added more structure to the app. I really like the guide I found.

**Thoughts**: Started using venv instead of pipenv, it's good to know both, but what I've noticed already is that pipenv was a lot more simpler.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 20: August 21, 2019

**Today's Progress**: Added working login form with validation and stuff. Ran into few errors, but all of them were of my mistyping mistakes. I liked the name of flask extension Flask-WTF.

**Thoughts**: I see how python/flask impacts code for web, all the simplified "for" loops and other things, I could only imagine what it would look like with more ugly languages like java.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 21: August 22, 2019

**Today's Progress**: Added database system, currently using SQLite.

**Thoughts**: Flask has nice extensions for databases so I didn't run into problems. I wonder how things will go when I want to migrate them to server, instead of using for localhost only.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 22: August 23, 2019

**Today's Progress**: I worked more on databases to prepare them for usage.

**Thoughts**: The whole database thing is a bit confusing, but I think I'll get it more when I'll see the big picture.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 23: August 24, 2019

**Today's Progress**: Added registration of the user and move improvements, but now the website is not working.

**Thoughts**: I've spent a lot of time trying to solve this bug, I hope I'll manage to fix it.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 24: August 25, 2019

**Today's Progress**: I've fixed the issue, now everything is working, I'll now be able to continue this project.

**Thoughts**: I also realized I've made some mistakes in other git projects instructions in the readme files, so I fixed that too.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 25: August 26, 2019

**Today's Progress**: Improved the structure of the website, added profile page and avatars.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 26: August 27, 2019

**Today's Progress**: Created the edit profile pages for users to change their information. Currently user can change username and "about me" info.

**Thoughts**: I got used to Atom, I don't know if I'll go back to visual studio code IDE. Unless necessary, because Atom is so uncluttered and clean and I don't come up with any errors that would be caused by IDE.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 27: August 28, 2019

**Today's Progress**: I added error handling and also now when error occurs I get an email with the error message, to spot errors when users are using the site.

**Thoughts**: Building this site is requiring more time than I anticipated, but that's ok, considering I've never worked with flask before.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 28: August 29, 2019

**Today's Progress**: I've added the functionality of follower/following and learned to create test cases for testing project.

**Thoughts**: I can now imagine how QA dev workflow looks like, creating test cases to test all scenarios.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 29: August 30, 2019

**Today's Progress**: Added functionality of writing a post and deleted fake posts. Because of this, a user now sees posts of other users in the index/home page.

**Thoughts**: I've found out you can resize the post writing form, I'll have to make it fixed.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 30: August 31, 2019

**Today's Progress**: Added pagination functionality. Pagination is used to only load a certain amount of content into the page. Also added the buttons to go between pages of posts "Older/Newer". Also, there's now explore page to find other users and see everyone's posts.

**Thoughts**: By functionality, this page is very similar to twitter right now.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 31: September 1, 2019

**Today's Progress**: Added the functionality to reset your password if you forget it. Ran into a few bugs, but managed to solve them.

**Thoughts**: Basically the structure and functionality of the website is complete and I will start to work on the front side soon.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 32: September 2, 2019

**Today's Progress**: Updated the site visually with bootstrap. It now looks decent and consistent in style and there's actually less code now.

**Thoughts**: I remember when I first started working with web development, a few years ago, I used to switch my work on a website between functionality and visual parts and it would actually took more time. I really liked this approach, work only on the functionality and when it's done, then move on to the visual parts.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 33: September 3, 2019

**Today's Progress**: Reformatted date and time, started using flask-moment library. Messages now show, what time ago a post were posted.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 34: September 4, 2019

**Today's Progress**: Working with translations now.

**Thoughts**: Though translating is not a difficult task, it took me more time, since I had to go through all the files and check the strings to prepare them for translation extraction.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 35: September 5, 2019

**Today's Progress**: Initialized Lithuanian language and also added language translation cli. (Command Line Integrations)

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 36: September 6, 2019

**Today's Progress**: Started working on client side translations with ajax.

**Thoughts**: Had to create a Microsoft Azure account for translations API, but messed up my credit card info and can't continue right now. Will have to continue on this tomorrow.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 37: September 7, 2019

**Today's Progress**: Fixed the issue with Microsoft Azure and managed to get all the translation stuff working.

**Thoughts**: I spent a lot of time on fixing a bug. Everything seemed correct, but automatic translations would not work. After few hours of reading and trying out different code I've managed to fix it. That really made me happy!

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 38: September 8, 2019

**Today's Progress**: Changed the structure of the project, so that it would scale better.

**Thoughts**: Changing the structure caused a few problems, but it seems I've managed to solve them.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 39: September 9, 2019

**Today's Progress**: Started working toward search functionality. I'm using Elastic Search.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 40: September 10, 2019

**Today's Progress**: I've finished search functionality. The search bar is now fully working, although I've noticed that the search only finds full words, other than that it's working really well. I also ran into an error 405. Stack overflow helped me out. Turns out I wrote method POST instead of GET for the search form.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 41: September 11, 2019

**Today's Progress**: Started setting up for deploying website to an actual server. Currently I'll be using free software: VirtualBox and Vagrant.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 42: September 12, 2019

**Today's Progress**: https://programitter.herokuapp.com/ Finally, the website is up and running, although I found a bug, when I post something, the page crashes, but post is successfully submited to the database. I'll have to fix it another day.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 43: September 13, 2019

**Today's Progress**: Spent the whole time trying to fix the bug. Unsuccessfully still.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 44: September 16, 2019

**Today's Progress**: I'm still trying to fix the bug, but I gained some progress. The issue lies not on the database side, but on the requests side, since posts are submitted successfully, but redirection after submitting is not working properly, and you can just press "back" and everything's there with the new post.  

**Thoughts**: I took 2 days off of the challenge since I went on a weekend trip, but I haven't had any days off for about 5 weeks, so I think it's fair.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 45: September 17, 2019

**Today's Progress**: I DID IT, I FIXED THE BUG!!!! I was really getting frustrated with this bug, since posting is the main functionality of the website. Turns out it was a problem with multiple commits to the database, I needed to flush the database.

**Thoughts**: I even wrote a letter to the writer of the article, Michael Cho, a thank you letter.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 46: September 18, 2019

**Today's Progress**: So, there was only one bug left, that you couldn't press next/previous page buttons, or so I thought! After investigating the "bug", turns out there were not enough posts for the website to need another page for posts, so I decided to reduce the number of posts per page from 25 to 20. Also, since the website URL were programitter.herokuapp.com, I changes the title and names of the website to Programitter.

**Link(s) to work**: https://github.com/eXTure/Website-with-Flask/tree/master/microblog


### Day 47: September 19, 2019

**Today's Progress**: Since website is in a stable state, with no known bugs, I decided to move away from the website for now. I didn't have much time today, so instead of a project, I decided to do a coding challenge on PyBites. I chose a challenge with string manipulation. I managed to complete a part of the challenge, but I still need to address more difficult cases.

**Thoughts**: I'll be moving back to coding school project.

**Link(s) to work**: https://github.com/eXTure/code-playground/blob/master/string_rotation.py


### Day 48: September 20, 2019

**Today's Progress**: Still working on the string manipulation. It's harder than I thought. I've tested out a few versions, but none of them could pass all tests provided by the PyBites, so I'll keep working on it.

**Link(s) to work**: https://github.com/eXTure/code-playground/blob/master/string_rotation.py


### Day 49: September 21, 2019

**Today's Progress**: I got back to the video content measuring tool project. Didn't code much, since the work included other tasks.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 50: September 22, 2019

**Today's Progress**: More data model preparation work.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 51: September 23, 2019

**Today's Progress**: Finished with the image set, all annotated and in VOC format. Having some problems with darknet.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 52: September 24, 2019

**Today's Progress**: Trying out darkflow/darknet on Ubuntu.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 53: September 25, 2019

**Today's Progress**: I've managed to run the training of the model on ubuntu, but the laptop couldn't handle such intense task, since it's an old laptop. I'll have to figure it out in some other way.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 54: September 26, 2019

**Today's Progress**: I've manage to start linux ubuntu on VirtualBox and did everything that's neccessary to start training the model. So now I have to PC's in training mode. I wonder how long it will take to finish the training, since the laptop is already training for full 24 hours!

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 55: September 27, 2019

**Today's Progress**: Turns out you have to stop the training manually and I was running the training for more than 2 days, and I was nearing the "overfitting". Trying to figure out how to train my own model.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 55: September 28, 2019

**Today's Progress**: Worked with string rotation challenge, since I've been writing very little code on other days.

**Link(s) to work**: https://github.com/eXTure/code-playground/blob/master/string_rotation.py


### Day 56: September 29, 2019

**Today's Progress**: I finished the challenge, string is now rotated correctly.

**Thoughts**: Turns out the correct solution was so simple and short, it was a 1 line solution and I wrote about 40 lines...

**Link(s) to work**: https://github.com/eXTure/code-playground/blob/master/string_rotation.py


### Day 57: September 30, 2019

**Today's Progress**: Working on a classifier, ran into problems with ubuntu versions. I'll try the same on a laptop.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 58: October 1, 2019

**Today's Progress**: Managed to plow through some of the bugs/error and ran into more bugs and errors. All in all, a productive day, since I moved forward a bit.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 59: October 2, 2019

**Today's Progress**: Tried out some other solutions, but none of them were what I needed.

**Link(s) to work**:


### Day 60: October 3, 2019

**Today's Progress**: After more digging, I'm starting to get a clearer picture of what I need to do, but I'm not there yet. Tried out a few scripts.

**Thoughts**: Actually, yesterday I forgot to push log update to github.

**Link(s) to work**: https://github.com/eXTure/Video-Content-Measuring-Tool


### Day 61: October 3, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 62: October 4, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 63: October 5, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 64: October 6, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 65: October 7, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 66: October 8, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 67: October 9, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 68: October 10, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 69: October 11, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:


### Day 70: October 12, 2019

**Today's Progress**:

**Thoughts**:

**Link(s) to work**:
