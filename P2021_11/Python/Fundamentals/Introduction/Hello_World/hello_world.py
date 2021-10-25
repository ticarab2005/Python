# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", "Noelle", "!")	# with a comma
print("Hello" + " " + "Noelle!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", 42)	# with a comma
print("Hello" + (str(42)))
# print("Hello" + 42)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

name = "Ticara"
name = 34
fav_food1 = "pho"
fav_food2 = "fries"
print("Hello", "Ticara", "!")
print("Hello" + " " + "Ticara!")

print("Hello", 34)
print("Hello" + " " + (str(34)))

print("I love to eat {} and {}.".format(fav_food1, fav_food2))
print(f"I love to eat {fav_food1} and {fav_food2}.")

hT = "Hello %s" % "Ninjas!"
py = "I love coding python %d" % 3
print(hT, py)

name = "Ticara"
age = 34
print("My name is %s and I'm %d" % (name, age))
