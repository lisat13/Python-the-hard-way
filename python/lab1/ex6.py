#definerer x til en string (r)
x = "There are %d types of people." % 10
# def. binary som en string
binary = "binary"
# def. do_not til en string
do_not = "don't"
#def. y til en string med 10 variabler
y = "Those who know %s and those who %s." % (binary, do_not)

#skriver cariablene x og y
print x
print y
# printer en string med en variabel i
print "I said: %r." % x
print "I also said: '%s'." % y
#def. hilarious til false 
hilarious = False
# def. joke_evalution til string
joke_evaluation = "Isn't that joke so funny?! %r"
# skriver ut 10 variabler
print joke_evaluation % hilarious
#def. variabler til en string
w = "This is the left side of..."
e = "a string with a right side."
#skriver ut to variabler i en setning
print w + e
