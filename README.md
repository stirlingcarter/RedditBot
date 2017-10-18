# RedditBot

## About

Reddit bots are scripts running on various servers, such as Raspberry Pis or personal computers, which interact with Reddit.com's API in order to read and write Reddit comments in helpful or novel ways. This tutorial is meant to be an accessible guide to writing such a bot using Python, a simple language.

This guide is for anyone who can navigate their file system! It will take minutes for an expert, and hopefully not too much longer for someone who has a basic understanding of programming. 

### Getting started 

To get started, you'll need:
  1. a text editor (I recommend Visual Studio, but you could theoretically use notepad - just don't use a *rich* text editor such as      Word, which adds metadata to your file) and 
  2. an installation of [Python 3.6.x](https://www.python.org/downloads/release/python-363/) (a version starting with 3.6). If you're      using Windows you'll probably want to use the 64 bit MSI installer. 

Check to see if Python is installed by opening up a command prompt or terminal (type cmd into cortana or your start menu on windows), and typing python followed by the enter key. If the version isn't displayed, you need to reinstall or restart. If neither works, [add Python to your path](http://pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/). 

This <bb>*spooky*</bb> black window is a powerful tool that lends you better accessibility to your operating system. You can practice [here](http://hackertyper.com/). 

Go ahead and make a new text file on your desktop, or anywhere you like. This will be your bot! Feel free to paste the code found in bot.py into your text file, or just type in the code as we address each line in the steps below. 

#### Some info about Python for those who are interested

Python is a widely used language that uses an interpreter, instead of a compiler, to generate machine code (1's and 0's that your computer outputs as useful displays such as text or photos). This means that every line generates a corresponding instruction for your machine, whereas a compiled language such as C++ is processed by a complicated chain of events to generate a meaningful machine code executable file (files are linked together, functions are expanded, and code is optimized). Because you don't have to recompile a Python file every time you change it, it is really nice to work with - fast to develop with and light on system resources. A lot of supercomputers are written in Python! 

### Step 1 - Libraries
Since Python is so nice to work with, there is a huge community and a lot of libraries written in Python. A library could be as simple as a Python file that has a list of English words, which could be included in a spellchecking program, or as complicated as a set of files that provide machine learning capabilities. We'll use PRAW, a library written by Reddit developers for interacting with Reddit.com, with the import statement on line 2. Line 1 is preceded by a #, which is why our computer ignores it - it's just a comment for humans. Comments are extremely important for readability so it's good to get in the habit of using them generously. 

### Step 2 - Make a Reddit account
Next, you'll need to make a Reddit account for your bot. Once it's created, access your settings and click the app tab. Name the bot as you wish, label it as a script, and enter in an optional set of info webpages. Click Create App, and take note of all the numbers you see on the next page - PRAW will use them to read and write reddit comments! 

### Step 3 - The constructors
This section of our code relies completely on [PRAW](http://praw.readthedocs.io/en/latest/index.html). It's very readable - don't be intimidated by the documentation and don't hesitate to dive in if anything is confusing to you. Reading docs is an extremely important skill in the software development world. 

Line 5 is the beginning of the constructor. This instantiates a bot using instructions from the PRAW library. The user agent is up to you, but the other 4 strings are very important. Enter your password, username, client secret, and client id (the unlabeled string next to the bot icon) so that PRAW has enough information to post a comment and access the website. 

Line 12 initiates a subreddit. If you chose 'all', you'll be parsing through a lot of comments, so make sure your computer is prepared for the load.

Line 16 initiates a *comment stream*. This is a running queue of comments from the given subreddit, accessed one at a time with the next control structure - a *for in* loop. 

### Step 4 - The comment stream
The block starting at line 19 takes each comment one by one and extracts the text. So far, it just prints the text to your screen if the keyword 'example' is found in the text, but this is where your creativity comes in - everything you need to continue can be found by googling PRAW operations like commenting, or Python operations like text parsing. Some things to keep in mind:
  - Run your script by giving it a py extension and double clicking it. You can also navigate to the containing folder in your             terminal with the [cd](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands) command and type py example.py           followed by enter, but the .py extension is not optional. 
  - Your comments will be limited to a frequency of 1 comment per several mins until you amass a certain amount of upvotes.
  - Your script will run until an error appears or you close the program. 
  - There are [thousands](https://github.com/stirlingcarter/TranslateBot) of examples of bots all over the internet - read through 1       and you'll feel much more prepared to write your own. Read through 20 and you'll be dangerous. 
  
  
##### Thanks for reading! Don't hesitate to reach out at stirling.h.carter@vanderbilt.edu if you have questions or want to share your super cool bot. 




