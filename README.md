Project 5: Web Crawler

Important! Sometimes the program will not execute properly, and print: "Error: No login token" and sys exit. Just rerun it.
Other than the error print, the terminal will give a more confusing href KeyError sometimes(depends on the code version I ended up submiting). Rerun that too.

The program takes a while to run, even with all the performance improvements that I made. It will almost always take less than 30 minutes to run, especially locally.

3700crawler
This is the primary class of this project: it login into fakebook and crawls through each page to find the flags. The main method 
here is the run method, which does the login process, after which the program reaches the crawl method, which crawls through 
fakebook and accesses new links to find the flags. I have a send method which is now only for the run() part, and a send_crawl method which I implemented to read content-length and work with one socket. I have a get_linked_urls method which I optimized pretty well. The run and crawl method may look long, but exluding comments and spaces, they are less than 50 lines.

parser1.py
This is the helper class for the 3700 crawler. It parses through the html content. It helps find the csrf token, flag, and url.
The main method here is the handle_start_tag method, which parses the information based on the tag and the parse_type. I spent the vast majority of my time on the crawler class though

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
Runtime-
Runtime was absolutely abmyssal though. To improve the runtime, I used set instead of list for urls_to_visit and visited_urls, I remade my program to not use a new socket each crawl iteration, and more.

Testing:
Testing was rather difficult. For both logging in and crawling, I shoved a large number of prints in order to debug any problems, and I later deleted or commented them out. For login I would print out entire htmls and repsonses to ensure that every step was done correctly. For the crawl I ran through the code with a ton of prints, like the whole response, to debug it. After I switched to one socket, I got partially cut responses, which I didn't know at first. I would run the code and only 2 to 4 flags would come, so I spent a while waiting for tests to finish and figure out the problem (In the end I made the send_crawl). Using extensive prints will usually reveal potential issues without waiting for the entire code to run, and I wish I used prints more generously than I did at first.
