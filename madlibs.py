def user_input(prompt):
	user_input = input(prompt)
	return user_input

def clear():
	print("\033[H\033[J")

def sci_fi():
	clear()
	
	noun1 = user_input("Pick a noun: ")
	clear()
	name = user_input("Pick a name: ")
	clear()
	clothing = user_input("Pick a piece of clothing: ")
	clear()
	color = user_input("Pick a color: ")
	clear()
	creature = user_input("Pick a creature: ")
	clear()
	number = user_input("Pick a number: ")
	clear()
	weapon = user_input("Pick an object: ")
	clear()
	weapon2 = user_input("Pick another object: ")
	clear()
	movement = user_input("Pick a movement: ")
	clear()
	
	print("The spaceship approached the landing " + noun1 + ". As the thrusters engaged " + name + " was yanked out of his " + clothing + ", and coffee covered the floor. The doors opened, surprisingly, the spacestation was deserted. " + color + " slime was splattered all over the walls and the smell of " + creature + "s was rampant. Two men came running from around the corner wielding " + weapon + "s and shouting \"The " + creature + "s are coming!\". " + number + " " + creature + " scurried across the ceiling leaving a " + color + " trail. " + name + " picked up the " + weapon2 + " from off of the floor, and with a spinning " + movement + ", sliced the " + creature + "s in half.")

def western():
	clear()

	noun1 = user_input("Pick a noun: ")
	clear()
	name = user_input("Pick a name: ")
	clear()
	clothing = user_input("Pick a piece of clothing: ")
	clear()
	color = user_input("Pick a color: ")
	clear()
	creature = user_input("Pick a creature: ")
	clear()
	number = user_input("Pick a number: ")
	clear()
	weapon = user_input("Pick an object: ")
	clear()
	weapon2 = user_input("Pick another object: ")
	clear()
	movement = user_input("Pick a movement: ")
	clear()
	
	print("Howdy partner! exclaimed " + name + ". So you're the new sheriff in town. I thought you'd be " + adjective + ". ")

def select_story():
	print("[1]: Sci-Fi\n[2]: Western\n[3]: Horror")
	
	story = int(user_input("Choose a storyline [1 - 3]: "))
	if story == 1:
		sci_fi()
	elif story == 2:
		western()
	elif story == 3:
		horror()
	else:
		clear()
		print("Invalid input")
		select_story()

clear()
select_story()	 
