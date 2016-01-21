# Defins madlibs function
def madlibs():
    print "Welcome to Mad Libs Game."
    print "You should enter some information to make this game work."

    # Make the player input the variables in order to output later.
    adj_1 = raw_input("Enter an adjective\n> ")
    v_1 = raw_input("Enter an 'ing' verb\n> ")
    n = raw_input("Enter a noun\n> ")
    v_2 = raw_input("Enter a plural present tense verb\n> ")
    place = raw_input("Enter a place\n> ")
    name = raw_input("Enter a person's name\n> ")
    adj_2 = raw_input("Enter an adjective\n> ")

    # Printing out the story including the inputs that the players had entered
    print """    I am a/an %s SCS student. I am proud of myself!
I always enjoy %s at school. I will introduce my friend.
This is my best friend %s. We always %s together.
When we do that, we go to %s.""" % (adj_1, v_1, n, v_2, place)
    print """    My favorite teacher is %s. He/she is very %s.
I love him/her because of this attribute.""" % (name, adj_2)

# Starts the function
madlibs()
