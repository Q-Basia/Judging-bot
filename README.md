# Judging-bot

This bot was created for HACKED 2023 to help the admin run the judging more smoothly.

Based on what the teams wanted, the teams could choose whther to present their project either in person or online and the bot would arrange the teams into two groups, 
in-person and online

This bot has 3 main functions:
- order()
- nextO()
- nextI()

order():
This function is to display all the teams who have decided to enter their projects for judging and order them so that the teams know when they are up next. It returns 
a dictionary that will be used by the other functions. It is only called once.

nextO():
This function uses the dictionary and uses it to find out who is next in line. It calls the next team who is up next in the online category and tell the next team in 
line to get ready. Then it removes the team that was judged from the dictionary and returns the dictionary.

For the purpose and nature of the event, to make the judging faster, there are two duplicates of this function. So the dictionary is used by all thre functions and is 
updated everytime one iof the functions is called so that no team is called twice (reason for popping of the team when it has been called for judging)

nextI():
This function is to call the next team who is up next in the inperson category and tell the next team in line to get ready


