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

**Today's Progress**: -

**Thoughts**: -

**Link(s) to work**:


### Day 15: August 15, 2019

**Today's Progress**: -

**Thoughts**: -

**Link(s) to work**:
