# Defins madlibs function
def madlibs():
    print "Welcome to Mad Libs Game."
    print "You should enter some information to make this game work."

    # Make the player input the variables in order to output later.
    adjective_1 = raw_input ("Enter an adjective\n> ")
    verb_1 = raw_input ("Enter an 'ing' verb\n> ")
    noun = raw_input ("Enter a noun\n> ")
    verb_2 = raw_input ("Enter a plural present tense verb\n> ")
    place = raw_input ("Enter a place\n> ")
    person_name = raw_input ("Enter a person's name\n> ")
    adjective_2 = raw_input ("Enter an adjective\n> ")

    # Printing out the whole story including the inputs that the players had entered
    print """    I am a/an %s SCS student. I am proud of myself!
I always enjoy %s at school. I will introduce my friend.
This is my best friend %s. We always %s together.
When we do that, we go to %s.
    My favorite teacher is %s. He/she is very %s.
I love him/her because of this attribute.""" %(adjective_1, verb_1, noun, verb_2, place, person_name, adjective_2)

# Starts the function
madlibs()
