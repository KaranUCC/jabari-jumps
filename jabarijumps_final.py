'''
Text-based game for students in grades 1-3 designed to create a fun and engaging way to test their knowledge and promote learning

Book: Jabari Jumps by Gaia Cornwall

Karan Maheshwari Y9

2022
'''

# imports
import time
import os
import sys
import termcolor
import webbrowser
from playsound import playsound

# automatically enlarges the terminal screen for the game
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=60, cols=206))

# a function that takes in a string and prints it out one character at a time with 0.05 seconds in between characters
def delayprint(str):

   for i in range(0, len(str)):

		# though this time to too slower for the average user, this game is designed for students in grades 1-3 who naturally have slower reading times
      time.sleep(0.05)

		# end='' allows the function to print each letter next to eachother and not on another line
      print(str[i], end='')

		# removes the buffer in terminal and creates the delayed text effect
      sys.stdout.flush()
   print('')

# a function for the loading sign in my game so that I dont have to write this large ascii text everywhere
def loading():

	# os.system('clear') blacks out the terminal as if its a new page
	os.system('clear')

	# termcolor is an easy way to print colored text
	termcolor.cprint('''\n
	██       ██████   █████  ██████  ██ ███    ██  ██████           
	██      ██    ██ ██   ██ ██   ██ ██ ████   ██ ██                
	██      ██    ██ ███████ ██   ██ ██ ██ ██  ██ ██   ███          
	██      ██    ██ ██   ██ ██   ██ ██ ██  ██ ██ ██    ██   ████   ████   ████    
	███████  ██████  ██   ██ ██████  ██ ██   ████  ██████    ████   ████   ████
	''', 'yellow')

	# delays the next python line from running by 1 second
	time.sleep(1)
	os.system('clear')

# a function to print the "correct" ascii word when you get a question right
def correctText():

	# uses playsound to play an mp3 audio file
	# using False allows the sound to play simultaneously with the code
	playsound("correct.mp3", False)

	# attrs=['blink'] is a feature termcolor has that can make text blink 
	termcolor.cprint('''\n
     ██████  ██████  ██████  ██████  ███████  ██████ ████████     ██████ 
    ██      ██    ██ ██   ██ ██   ██ ██      ██         ██         ████ 
    ██      ██    ██ ██████  ██████  █████   ██         ██          ██ 
    ██      ██    ██ ██   ██ ██   ██ ██      ██         ██           
     ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██          ██ 
	''', 'green', attrs=['blink'])

	time.sleep(1)

# a function to print the "try again" ascii word when you get a question wrong
def incorrectText():

	# printing "wrong" is discouraging and as apart of my criteria, I want to print a positive message so I used "try again" promting the user the keep trying
	termcolor.cprint('''\n
    ████████ ██████  ██    ██      █████   ██████   █████  ██ ███    ██     ██████ 
       ██    ██   ██  ██  ██      ██   ██ ██       ██   ██ ██ ████   ██      ████ 
       ██    ██████    ████       ███████ ██   ███ ███████ ██ ██ ██  ██       ██ 
       ██    ██   ██    ██        ██   ██ ██    ██ ██   ██ ██ ██  ██ ██        
       ██    ██   ██    ██        ██   ██  ██████  ██   ██ ██ ██   ████       ██  
	''', 'red', attrs=['blink'])

	time.sleep(1)


# introduction that collects basic information like the users name and if they already know how to play
def introduction():

	# these variables are now global so I can use them again outside of this function
	global name
	global canPlay

	termcolor.cprint('''\n
         ██  █████  ██████   █████  ██████  ██          ██ ██    ██ ███    ███ ██████  ███████         ████████ ██   ██ ███████      ██████   █████  ███    ███ ███████ 
         ██ ██   ██ ██   ██ ██   ██ ██   ██ ██          ██ ██    ██ ████  ████ ██   ██ ██       ██        ██    ██   ██ ██          ██       ██   ██ ████  ████ ██      
         ██ ███████ ██████  ███████ ██████  ██          ██ ██    ██ ██ ████ ██ ██████  ███████            ██    ███████ █████       ██   ███ ███████ ██ ████ ██ █████   
    ██   ██ ██   ██ ██   ██ ██   ██ ██   ██ ██     ██   ██ ██    ██ ██  ██  ██ ██           ██  ██        ██    ██   ██ ██          ██    ██ ██   ██ ██  ██  ██ ██      
     █████  ██   ██ ██████  ██   ██ ██   ██ ██      █████   ██████  ██      ██ ██      ███████            ██    ██   ██ ███████      ██████  ██   ██ ██      ██ ███████                                                                                                                                                                   
    ''', 'cyan', attrs=['blink'])

	time.sleep(1)

	delayprint(termcolor.colored('\n    Turn the sound up !!'))

	# this is used to stop the code from continuing until the user wants to. It acts like a red light
	# the code will only continue after the user presses enter, giving them enough time to look at everything
	delayprint('\n    PRESS ENTER TO PLAY')
	input('    ')

	loading()

	# gets the users name
	# \n is used to create a new line and is soley there to make everything look nice and neat on the terminal
	delayprint('\n\n    What is your name?\n\n    ')

	# the \033[92m changes the color of what the user types to green to distinguish the games text from the users
	# I cannot use termcolor on a input statement so i used this instead
	name = input('\033[92m    ')

	# a while loop is used so that the question is repeated if the user types an invalid response
	while True:

		# sees if the user can play or do they require a tutorial
		# the \033[0m changes the color back to white so that everything is not green
		# termcolor does not have the color white so I cannot use it here
		delayprint('\033[0m\n\n    Do you know how to play?\n')
		delayprint('    1. Yes\n    2. No\n')

		# it is nessecary to write this as i haven't explained the game yet so i cant expect new users to know how to respond
		delayprint('\n    Please type a number related to your answer')

		canPlay = input('\033[92m\n    ')

		# if they cannot play, they go through the tutorial
		if canPlay == '2':

			delayprint("\033[0m\n\n    Let's go through a tutorial on how to play!\n")
			delayprint('\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()
			# returning false ends the loop
			return False

		# if they can play, they start the game immediately
		elif canPlay == '1':

			termcolor.cprint("\n\n    Let's start the game!\n", 'red', attrs=['blink', 'bold'])

			time.sleep(1)

			delayprint('\n    PRESS ENTER TO PLAY')
			input('    ')

			loading()
			return False

		else:

			# this is the invalid message statement that prints and notice that it doesn't return false afterwards meaning it repeats the question
			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

# the tutorial which explain in text how the game is played, the rules, and how the point system works
def tutorial():

	termcolor.cprint('''\n
    ████████ ██    ██ ████████  ██████  ██████  ██  █████  ██      
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██      
       ██    ██    ██    ██    ██    ██ ██████  ██ ███████ ██      
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██      
       ██     ██████     ██     ██████  ██   ██ ██ ██   ██ ███████ 
	''', 'cyan')

	# i have to change the color outside the string since I cannot change it in the middle of a multiline string
	purple = termcolor.colored('purple', 'magenta')

	# writing f before the apostrophe allows me to easily input a variable into a string using {}
	# using multiline code instead of singular
	delayprint(f'''\n\n    You will be given a question in {purple} about Jabari Jumps.

	\n    Then, below the question there are numbered answers in the color white.

	\n    You must choose the correct answer and type the corresponding number.

	\n    Make sure to press enter after typing your choosen number.

	\n    If you are correct, you will move onto the next question.

	\n    If you are incorrect, the game will promt you with the same question till you get it right.

	\n    Your score will be how long it took you to complete the quiz.
	''')

	delayprint('\n    PRESS ENTER AFTER READING')
	input('    ')

	delayprint("\n    Let's go through some practice questions!\n")

	delayprint('\n    PRESS ENTER TO CONTINUE')
	input('    ')

	loading()

# practise questions to help familiarize the user with the game format
def tutorialQuestion1():

	termcolor.cprint('''\n
    ████████ ██    ██ ████████  ██████  ██████  ██  █████  ██           ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██ 
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██          ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ███ 
       ██    ██    ██    ██    ██    ██ ██████  ██ ███████ ██          ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██ 
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██          ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██      ██ 
       ██     ██████     ██     ██████  ██   ██ ██ ██   ██ ███████      ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██ 
                                                                           ▀▀                                                                       
	''', 'cyan')

	# helps keep things slow and not too overwhelming
	time.sleep(0.5)

	# used to count the seconds it took the user to answer the question
	# this starts the clock
	ticTQ1 = time.perf_counter()

	while True:

		# prints the question and options
		delayprint(termcolor.colored('\n\n    What color is the sky?', 'magenta'))
		delayprint('\n    1. Red\n    2. Blue\n    3. Green\n\n')

		# collects the response and assigns it a variable
		tutorialQuestion1 = input('    \033[92m')

		# checks for the correct response
		if tutorialQuestion1 == '2':

			correctText()

			# stops the clock
			tocTQ1 = time.perf_counter()

			# get the seconds, rounds it to the nearest tenth, and assigns the time a variable so that i can use it in a string
			time_TQ1 = round(tocTQ1 - ticTQ1, 1)

			# prints the time it took to answer the question
			delayprint(f'\n    You answered this question in \033[92m {time_TQ1} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		# checks for wrong answers and repeats question
		elif tutorialQuestion1 == '1':

			incorrectText()

		elif tutorialQuestion1 == '3':

			incorrectText()

		# checks for invalid answers and repeats question
		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

# last tutorial question
def tutorialQuestion2():

	# allows me to later check if the user wants to play the tutorial again
	global tutorialAgain

	termcolor.cprint('''\n
    ████████ ██    ██ ████████  ██████  ██████  ██  █████  ██           ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ██████  
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██          ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██          ██ 
       ██    ██    ██    ██    ██    ██ ██████  ██ ███████ ██          ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      █████  
       ██    ██    ██    ██    ██    ██ ██   ██ ██ ██   ██ ██          ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██     ██      
       ██     ██████     ██     ██████  ██   ██ ██ ██   ██ ███████      ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████     ███████ 
                                                                           ▀▀                                                                       
	''', 'cyan')

	time.sleep(0.5)

	ticTQ2 = time.perf_counter()

	while True:

		delayprint(termcolor.colored('\n\n    What shape has only 3 sides?', 'magenta'))
		delayprint('\n    1. Circle\n    2. Square\n    3. Triangle\n\n')

		tutorialQuestion2 = input('    \033[92m')

		# checks for correct answer
		if tutorialQuestion2 == '3':

			correctText()

			tocTQ2 = time.perf_counter()

			time_TQ2 = round(tocTQ2 - ticTQ2, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_TQ2} seconds')

			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			delayprint('\n\n    Looks like you know how to play now')

			time.sleep(1)

			# asks the user if they want to play again incase they forgot or any other reason
			while True:

				delayprint('\n    Do you want to play the tutorial again?')

				delayprint('\n    1. Yes\n    2. No\n\n')

				tutorialAgain = input('\033[92m\n    ')

				if tutorialAgain == '1':

					loading()
	# the tutorial functions won't be called here and will intead be called at the end of all this code

					return False

				elif tutorialAgain == '2':

					delayprint('\033[0m\n\n    In that case...')

					# starting the actual game now
					termcolor.cprint("\n    Let's start the real game now !", 'red', attrs=['blink', 'bold'])

					time.sleep(1)

					delayprint('\n    PRESS ENTER TO PLAY')
					input('    ')

					return False

				else:

					delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

			return False

		# checks for wrong answer
		elif tutorialQuestion2 == '1':

			incorrectText()

		elif tutorialQuestion2 == '2':

			incorrectText()

		# checks for invalid answer
		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

	# as you can see, i dont call any game related functions here because i will call them all in a function at the end

# prints the opening message to the game reminding the user of the rules and a positive message
def realGame():

	loading()

	delayprint('''\n\n    Remember, your score will be how long it took you to complete the quiz.

    Don't feel sad if you take a lot of time, this is just a game :)

    This game is designed to test your knowledge of Jabari Jumps and you can always take it again!

    Remember to have fun! That's what games are all about!
    ''')

	delayprint('\033[0m\n    PRESS ENTER TO PLAY')
	input('    ')

	loading()

# question 1
def question1():

	# making it global so i can use it to tally the score at the end
	global time_Q1

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██ 
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ███ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██      ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██ 
        ▀▀                                                                   
	''', 'cyan')

	time.sleep(0.5)

	# starting clock
	ticQ1 = time.perf_counter()

	while True:

		# printing the question and possible responses is included in the total time as it accounts for reading time
		delayprint(termcolor.colored('\n\n    What characters do we see first and where are they?', 'magenta'))
		delayprint('\n    1. Jabari is with his mom and dad at the pool\n    2. Jabari is with his mom and sister at the pool\n    3. Jabari is with his dad and sister at the pool\n    4. Jabari is with his sister at the pool\n    5. Jabari is with his friends at the pool\n\n')

		question1 = input('    \033[92m')

		# checking for right, wrong, or invalid messages
		if question1 == '3':

			correctText()

			# ending clock
			tocQ1 = time.perf_counter()

			time_Q1 = round(tocQ1 - ticQ1, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q1} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question1 == '1':

			incorrectText()

		elif question1 == '2':

			incorrectText()

		elif question1 == '4':

			incorrectText()

		elif question1 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

# --------- questions 1-10 all follow the exact same format so commenting on that code would be redundant ----------

def question2():

	global time_Q2

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ██████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██          ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      █████  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██     ██      
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████     ███████ 
        ▀▀                                                                       
   ''', 'cyan')

	time.sleep(0.5)

	ticQ2 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    What is Jabari's goal?", "magenta"))
		delayprint("\n    1. To finish his swim lessons\n    2. To pass his swim test\n    3. To practice his doggy paddle\n    4. To jump off the diving board\n    5. Jabari doesn't have a goal\n\n")

		question2 = input('    \033[92m')

		if question2 == '4':

			correctText()

			tocQ2 = time.perf_counter()

			time_Q2 = round(tocQ2 - ticQ2, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q2} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question2 == '1':

			incorrectText()

		elif question2 == '2':

			incorrectText()

		elif question2 == '3':

			incorrectText()

		elif question2 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question3():

	global time_Q3

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ██████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██          ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      █████  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██          ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████     ██████  
        ▀▀                                                                       
   ''', 'cyan')

	time.sleep(0.5)

	ticQ3 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    How is Jabari feeling towards jumping off the diving board?", "magenta"))
		delayprint("\n    1. Angry\n    2. Confident\n    3. Nervous\n    4. Sad\n    5. Neutral\n\n")

		question3 = input('    \033[92m')

		if question3 == '2':

			correctText()

			tocQ3 = time.perf_counter()

			time_Q3 = round(tocQ3 - ticQ3, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q3} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question3 == '1':

			incorrectText()

		elif question3 == '3':

			incorrectText()

		elif question3 == '4':

			incorrectText()

		elif question3 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question4():

	global time_Q4

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ██   ██ 
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ██   ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██     ███████ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██          ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████          ██ 
        ▀▀                                                                       
   ''', 'cyan')

	time.sleep(0.5)

	ticQ4 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    How do the other kids jump off the diving board?", "magenta"))
		delayprint("\n    1. They run off the diving board\n    2. They lay flat on the board and slide off\n    3. They sit on the edge and jump\n    4. They spread their arms and bend their legs\n    5. The kids dont jump from the diving board\n\n")

		question4 = input('    \033[92m')

		if question4 == '4':

			correctText()

			tocQ4 = time.perf_counter()

			time_Q4 = round(tocQ4 - ticQ4, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q4} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question4 == '1':

			incorrectText()

		elif question4 == '2':

			incorrectText()

		elif question4 == '3':

			incorrectText()

		elif question4 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question5():

	global time_Q5

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ███████ 
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ██      
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██     ███████ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██          ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████     ███████ 
        ▀▀                                                                       
   ''', 'cyan')

	time.sleep(0.5)

	ticQ5 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    How does Jabari feel after seeing the other kids jump?", "magenta"))
		delayprint("\n    1. Angry\n    2. Confident\n    3. Nervous\n    4. Sad\n    5. Neutral\n\n")

		question5 = input('    \033[92m')

		if question5 == '3':

			correctText()

			tocQ5 = time.perf_counter()

			time_Q5 = round(tocQ5 - ticQ5, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q5} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question5 == '1':

			incorrectText()

		elif question5 == '2':

			incorrectText()

		elif question5 == '4':

			incorrectText()

		elif question5 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question6():

	global time_Q6

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ██       
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██     ███████  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██     ██    ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██████  
        ▀▀                                                                        
    ''', 'cyan')

	time.sleep(0.5)

	ticQ6 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    What advice does Jabari's dad give him when he is feeling tired?", "magenta"))
		delayprint("\n    1. To keep climbing\n    2. To climb down and try tomorrow\n    3. To climb down and eat food for energy\n    4. To climb down and take a small rest\n    5. To climb down and rehydrate\n\n")

		question6 = input('    \033[92m')

		if question6 == '4':

			correctText()

			tocQ6 = time.perf_counter()

			time_Q6 = round(tocQ6 - ticQ6, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q6} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question6 == '1':

			incorrectText()

		elif question6 == '2':

			incorrectText()

		elif question6 == '3':

			incorrectText()

		elif question6 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question7():

	global time_Q7

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██     ███████ 
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██          ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██         ██  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██        ██   
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████        ██   
        ▀▀                                                                       
    ''', 'cyan')

	time.sleep(0.5)

	ticQ7 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    What advice does Jabari's father give him after he says he wants to try tomorrow?", "magenta"))
		delayprint("\n    1. Give up\n    2. Stretch more and try again\n    3. Eat more food for energy and try again\n    4. Try again tomorrow\n    5. It's okay to feel scared, take deep breaths and tell yourself that you are ready\n\n")

		question7 = input('    \033[92m')

		if question7 == '5':

			correctText()

			tocQ7 = time.perf_counter()

			time_Q7 = round(tocQ7 - ticQ7, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q7} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question7 == '1':

			incorrectText()

		elif question7 == '2':

			incorrectText()

		elif question7 == '3':

			incorrectText()

		elif question7 == '4':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question8():

	global time_Q8

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      █████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ██   ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      █████  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██     ██   ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      █████  
        ▀▀                                                                       
    ''', 'cyan')

	time.sleep(0.5)

	ticQ8 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    Does his father's advice help Jabari overcome his fear?", "magenta"))
		delayprint("\n    1. Yes and he jumps off the diving board\n    2. No and he decides to try tomorrow\n    3. Jabari ignores his fathers advice\n\n")

		question8 = input('    \033[92m')

		if question8 == '1':

			correctText()

			tocQ8 = time.perf_counter()

			time_Q8 = round(tocQ8 - ticQ8, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q8} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question8 == '2':

			incorrectText()

		elif question8 == '3':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question9():

	global time_Q9

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      █████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ██   ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██████ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██          ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      █████  
        ▀▀                                                                       
    ''', 'cyan')

	time.sleep(0.5)

	ticQ9 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    How does Jabari feel at the end?", "magenta"))
		delayprint("\n    1. Very happy :)\n    2. Sad\n    3. Neutral\n    4. Angry\n    5. Disappointed\n\n")

		question9 = input('    \033[92m')

		if question9 == '1':

			correctText()

			tocQ9 = time.perf_counter()

			time_Q9 = round(tocQ9 - ticQ9, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q9} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question9 == '2':

			incorrectText()

		elif question9 == '3':

			incorrectText()

		elif question9 == '4':

			incorrectText()

		elif question9 == '5':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

def question10():

	global time_Q10

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██  ██████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ███ ██  ████ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██ ██ ██ ██ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██      ██ ████  ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██  ██████  
        ▀▀                                                                            
    ''', 'cyan')

	time.sleep(0.5)

	ticQ10 = time.perf_counter()

	while True:

		delayprint(termcolor.colored("\n\n    What is Jabari's father's role throughout the book?", "magenta"))
		delayprint("\n    1. He discourages Jabari\n    2. He is irrelevant to the story\n    3. He supports and advises Jabari helping him overcome fear\n    4. He just watches Jabari\n    5. He teaches Jabari how to jump\n\n")

		question10 = input('    \033[92m')

		if question10 == '3':

			correctText()

			tocQ10 = time.perf_counter()

			time_Q10 = round(tocQ10 - ticQ10, 1)

			delayprint(f'\n    You answered this question in \033[92m {time_Q10} seconds')


			delayprint('\033[0m\n    PRESS ENTER TO CONTINUE')
			input('    ')

			loading()

			return False

		elif question10 == '1':

			incorrectText()

		elif question10 == '2':

			incorrectText()

		elif question10 == '3':

			incorrectText()

		elif question10 == '4':

			incorrectText()

		else:

			delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

# these are long answer questions with no time limit or right / wrong answer
def question11():

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██  ██ 
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ███ ███ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██  ██ 
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██      ██  ██ 
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██  ██ 
        ▀▀                                                                       
    ''', 'cyan')

	time.sleep(0.5)

	# explaining the rules
	delayprint('''\n\n    This is a special type of question.

	\n    It will not be timed and there are no wrong answers.

	\n    Your job is to answer the question with 1-2 sentences.

	\n    They won't be questions about the book, but questions about how you can apply the book to your life.

	\n    Remember, these special questions will not be timed and there are no wrong answers.
	''')

	delayprint('\n    PRESS ENTER AFTER READING')
	input('    ')

	# the question
	delayprint(termcolor.colored("\n\n    How can you be like Jabari's dad and support your friends in the classroom and help them overcome their fear?", "magenta"))

	# where the user types their long answer
	input('\n    \033[92m')

	# positive message
	delayprint('\033[0m\n    WOW, that was an amazing answer!!!')

	delayprint('\n    PRESS ENTER TO CONTINUE')
	input('    ')

	loading()

# same long answer type question
def question12():

	termcolor.cprint('''\n
     ██████  ██    ██ ███████ ███████ ████████ ██  ██████  ███    ██      ██ ██████  
    ██    ██ ██    ██ ██      ██         ██    ██ ██    ██ ████   ██     ███      ██ 
    ██    ██ ██    ██ █████   ███████    ██    ██ ██    ██ ██ ██  ██      ██  █████  
    ██ ▄▄ ██ ██    ██ ██           ██    ██    ██ ██    ██ ██  ██ ██      ██ ██      
     ██████   ██████  ███████ ███████    ██    ██  ██████  ██   ████      ██ ███████ 
        ▀▀                                                                           
    ''', 'cyan')

	time.sleep(0.5)

	delayprint('''\n\n    This is another special question like the one before.

	\n    Remember, these special questions will not be timed and there are no wrong answers.

	\n    You must write 1-2 sentences as your answer.
	''')

	delayprint('\n    PRESS ENTER AFTER READING')
	input('    ')

	delayprint(termcolor.colored("\n\n    What do you think the meaning behind this book is?", "magenta"))

	input('\n    \033[92m')

	delayprint('\033[0m\n    WOW, another amazing answer!!!')

	delayprint('\n    PRESS ENTER TO FINISH')
	input('    ')

	loading()

# this is the word search
# this section is used to expose the user to the UNSDG's and relate it to key words in the book
def wordSearch():

   termcolor.cprint('''\n
    ██     ██  ██████  ██████  ██████      ███████ ███████  █████  ██████   ██████ ██   ██ 
    ██     ██ ██    ██ ██   ██ ██   ██     ██      ██      ██   ██ ██   ██ ██      ██   ██ 
    ██  █  ██ ██    ██ ██████  ██   ██     ███████ █████   ███████ ██████  ██      ███████ 
    ██ ███ ██ ██    ██ ██   ██ ██   ██          ██ ██      ██   ██ ██   ██ ██      ██   ██ 
     ███ ███   ██████  ██   ██ ██████      ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ 
   ''', 'cyan')

   time.sleep(0.5)

	# explaining the rules
   delayprint('''\n\n    This section will not be timed and there are no wrong answers.

   \n    In this section, you must choose a word that relates to Jabari Jumps.

   \n    Then, explore the different sources connected to the word.

   \n    After you complete this, you will be given your score.

   \n    You must explore each word and its sources!

   \n    Learn about each word and have fun!
   ''')

   delayprint('\n    PRESS ENTER TO CONTINUE')
   input('    ')

	# used as a counter for how many sources the user has visited so far
   sources = 0

   loading()

	# this loop will end when the user has looked at 5 sources as it says in the rules
   while sources < 5:

      delayprint(termcolor.colored('\n\n    Choose any word', 'magenta'))

      # the list of words the user can pick from
      delayprint('\n    1. Fear\n    2. Water\n    3. Swimming Pool\n    4. Swimming\n    5. Support\n\n')

      word = input('    \033[92m')

      # checks for the word chosen
      if word == '1':

         loading()

         # shows the option choosen
         delayprint(termcolor.colored('\n\n    You chose Fear!', 'cyan', attrs=['bold']))

         # explains relevance to the book, what the website talks about, what to look for when reading, and further intructions
         delayprint('''\n\n    Jabari expierences fear throughout the book when watching the other kids jump and when he finally decides to jump.

         \n    Explore this website that talks about health and well-being from the United Nations (UN).

         \n    As you are reading, try and relate the website back to Jabari and how he expierences fear.

         \n    When you are done reading, return to this page and continue.
         ''')

         delayprint('\n    PRESS ENTER TO CONTINUE')
         input('    ')
         loading()

         # webbrowser.open open the given url in the user's default browser
         # this automatically opens the website without the user having to do anything
         webbrowser.open('https://sdgs.un.org/goals/goal3')

         # adds 1 to the sources counter
         sources += 1

         delayprint('\n\n\n    PRESS ENTER ONCE DONE')
         input('    ')
         loading()
		# same format for the second question but different website and things to look for on the website
      elif word == '2':

         loading()

         delayprint(termcolor.colored('\n\n    You chose Water!', 'cyan', attrs=['bold']))

         delayprint('''\n\n    The entire book is based around water.

         \n    Explore this website that talks about clean water and sanitation from the United Nations (UN).

         \n    As you are reading, reflect the water you use on a daily basis and sanitation systems at school and at home.

         \n    When you are done reading, return to this page and continue.
         ''')

         delayprint('\n    PRESS ENTER TO CONTINUE')
         input('    ')
         loading()

         webbrowser.open('https://sdgs.un.org/goals/goal6')

         sources += 1

         delayprint('\n\n\n    PRESS ENTER ONCE DONE')
         input('    ')
         loading()

      elif word == '3':

         loading()

         delayprint(termcolor.colored('\n\n    You chose Swimming Pools!', 'cyan', attrs=['bold']))

         delayprint('''\n\n    The setting and location of Jabari Jumps is in a swimming pool.

         \n    Explore this website that talks about industry, innovation, infrastructure in our world from the United Nations (UN).

         \n    As you are reading, reflect on buildings and items that you use daily and require to be manufactured.

         \n    When you are done reading, return to this page and continue.
         ''')

         delayprint('\n    PRESS ENTER TO CONTINUE')
         input('    ')
         loading()

         webbrowser.open('https://sdgs.un.org/goals/goal9')

         sources += 1

         delayprint('\n\n\n    PRESS ENTER ONCE DONE')
         input('    ')
         loading()

      elif word == '4':

         loading()

         delayprint(termcolor.colored('\n\n    You chose Swimming!', 'cyan', attrs=['bold']))

         delayprint('''\n\n    Jabari said that he took swimming lessons and finished his swimming education.

         \n    Explore this website that talks about quality education in our world from the United Nations (UN).

         \n    As you are reading, reflect on the useful things you have learnt and who/what taught it to you.

         \n    When you are done reading, return to this page and continue.
         ''')

         delayprint('\n    PRESS ENTER TO CONTINUE')
         input('    ')
         loading()

         webbrowser.open('https://sdgs.un.org/goals/goal4')

         sources += 1

         delayprint('\n\n\n    PRESS ENTER ONCE DONE')
         input('    ')
         loading()

      elif word == '5':

         loading()

         delayprint(termcolor.colored('\n\n    You chose Support!', 'cyan', attrs=['bold']))

         delayprint('''\n\n    Jabari's dad supports him throughout the book by advising and encouraging Jabari.

         \n    Explore this website that talks about different countries supporting and helping eachother achieve goals.

         \n    Specifically the United Nations Sustainability Development Goals.

         \n    As you are reading, reflect on how you and your classmates support eachother in achieveing your own goals.

         \n    When you are done reading, return to this page and continue.
         ''')

         delayprint('\n    PRESS ENTER TO CONTINUE')
         input('    ')
         loading()

         webbrowser.open('https://sdgs.un.org/goals/goal17')

         sources += 1

         delayprint('\n\n\n    PRESS ENTER ONCE DONE')
         input('    ')
         loading()

      else:

         delayprint(termcolor.colored('\n\n    THAT IS AN INVALID ANSWER\n\n    PLEASE TYPE A NUMBER LISTED BELOW', 'red'))

		# this section is purposely before the score ensuring that the user completes it
		# now the score will be shown
   delayprint("\n\n    Let's see your score and finish the game!")
   delayprint('\n\n\n    PRESS ENTER TO CONTINUE')
   input('    ')
   loading()

# the final score
def score():

	# for if the player wants to play again
	global playAgain

	termcolor.cprint('''\n
    ██    ██  ██████  ██    ██ ██████      ███████  ██████  ██████  ██████  ███████    ██████ 
     ██  ██  ██    ██ ██    ██ ██   ██     ██      ██      ██    ██ ██   ██ ██          ████ 
      ████   ██    ██ ██    ██ ██████      ███████ ██      ██    ██ ██████  █████        ██ 
       ██    ██    ██ ██    ██ ██   ██          ██ ██      ██    ██ ██   ██ ██             
       ██     ██████   ██████  ██   ██     ███████  ██████  ██████  ██   ██ ███████      ██ 
       ''', 'cyan')

	time.sleep(0.5)

	# adds up all the seconds from each question that was timed
	total_time = time_Q1 + time_Q2 + time_Q3 + time_Q4 + time_Q5 + time_Q6 + time_Q7 + time_Q8 + time_Q9 + time_Q10

	# formats the seconds into minutes for convenience using time.strftime and time.gmtime
	final_time = time.strftime("%M minutes and %S seconds", time.gmtime(total_time))

	# prints the final time
	delayprint(f'\n\n    Your score is \033[92m {final_time} !!')

	# prints a positive message
	termcolor.cprint('\n    That is an AMAZING score !!', 'cyan', attrs=['blink', 'bold'])

	delayprint('\n    PRESS ENTER TO CONTINUE')
	input('    ')

	os.system('clear')

	# asks the user if they would like the play again
	delayprint('\n\n    Do you want to play again?')

	delayprint('\n    1. Yes\n    2. No\n\n')

	# assigns the users answer as a variable for later use
	playAgain = input('\033[92m\n    ')

	if playAgain == '2':

		# prints goodbye message
		termcolor.cprint('''\n
	    ████████ ██   ██  █████  ███    ██ ██   ██     ██    ██  ██████  ██    ██     ███████  ██████  ██████      ██████  ██       █████  ██    ██ ██ ███    ██  ██████     ██████ 
	       ██    ██   ██ ██   ██ ████   ██ ██  ██       ██  ██  ██    ██ ██    ██     ██      ██    ██ ██   ██     ██   ██ ██      ██   ██  ██  ██  ██ ████   ██ ██           ████ 
	       ██    ███████ ███████ ██ ██  ██ █████         ████   ██    ██ ██    ██     █████   ██    ██ ██████      ██████  ██      ███████   ████   ██ ██ ██  ██ ██   ███      ██ 
	       ██    ██   ██ ██   ██ ██  ██ ██ ██  ██         ██    ██    ██ ██    ██     ██      ██    ██ ██   ██     ██      ██      ██   ██    ██    ██ ██  ██ ██ ██    ██        
	       ██    ██   ██ ██   ██ ██   ████ ██   ██        ██     ██████   ██████      ██       ██████  ██   ██     ██      ███████ ██   ██    ██    ██ ██   ████  ██████       ██ 
		''', 'cyan', attrs=['blink'])

		time.sleep(0.5)

# will put the google form relfection here for the user to answer

# this is where all the functions are called and the game comes together

def game():

	# first playes the introduction
	introduction()

	# if the user cannot play, then the tutorial and tutorial questions are run
	if canPlay == '2':

		tutorial()
		tutorialQuestion1()
		tutorialQuestion2()

		while True:

			# if the user wants to play the tutorial again, the tutorial functions are ran
			if tutorialAgain == '1':

				tutorial()
				tutorialQuestion1()

				# the user can choose if they would like to play the tutorial again or begin the actual game here
				tutorialQuestion2()

			# if they do not want to run the tutorial again, then the real game functions are run
			elif tutorialAgain == '2':

				realGame()
				question1()
				question2()
				question3()
				question4()
				question5()
				question6()
				question7()
				question8()
				question9()
				question10()
				question11()
				question12()
				wordSearch()
				score()

				if playAgain == '1':

					game()

				return False


	# if the user can play, then the actual game is run immediately
	elif canPlay == '1':

		realGame()
		question1()
		question2()
		question3()
		question4()
		question5()
		question6()
		question7()
		question8()
		question9()
		question10()
		question11()
		question12()
		wordSearch()
		score()

		# if playAgain is 1 (yes), the it runs this function again
		if playAgain == '1':

			game()

# calling the function game
game()

# Jabari Jumps: The game