Project 5: Web Crawler

Important! Sometimes the program will not execute properly, and print: "Error: No login token" and sys exit. Just rerun it.
I made the error print, because otherwise the terminal will give a more confusing href KeyError.

3700crawler
This is the primary class of this project: it login into fakebook and crawls through each page to find the flags. The main method 
here is the run method, which does the login process, after which the program reaches the crawl method, which crawls through 
fakebook and accesses new links to find the flags

parser1.py
This is the helper class for the 3700 crawler. It parses through the html content. It helps find the csrf token, flag, and url.
The main method here is the handle_start_tag method, which parses the information based on the tag and the parse_type

Challenges faced:
Login-
I spent a lot of time trying to login to Fakebook. The requests were very particular, and it was difficult to construct the
requests in the exact order with the required information. There was very little guides that I could find to help me do this,
and the feedback that I got from the terminal was not useful enough for me to debug effectively. I gathered the needed 
information for making requests by hardcoding: I split the responses into lines, retrieved the line I wanted based on the first 
word, and then located the word I needed. I cropped the word based on the characters, as needed. This was possible because the 
format was always the same, so I could print the response and manually look through it to see how I need to hardcode it. For a 
long time I wasn't getting urls, but eventually with proper POST and GET requests, this was fixed. 
Links and crawl-
I was able to search up some guides on how to use a Parser to retrive links using the -a starttag, and I was able to replicate 
this for csrf token as well. when I saw the h3 tag for flag in the project description, I added that to the Parser class as well.
I had some trouble getting urls while traversing fakebook, but this part was easier for me because i was able to find some  
resources online and it had a much better description in the project of how to complete this. 
Runtime(used to take like 40 minutes)-
Runtime was absolutely abmyssal though. To improve the runtime, I tried printing each time it looked for a url and each time it 
found it. It used to be like 5 to 15 times, so I tried some different methods like removing the url after use, but it barely 
helped. So I just used random, since going though the urls in order was taking sooo long.

Testing:
Testing was rather difficult. For both logging in and crawling, I shoved a large number of prints in order to debug any problems, and I later deleted or commented them out. For login I would print out entire htmls and repsonses to ensure that every step was done correctly. For the crawl I mainly had trouble with traversing past the first one or two links. I created a parser class tag and parse type for flag to ensure that it would be collected properly, since my runtime was rather bad, and finding flags took a long time. 
