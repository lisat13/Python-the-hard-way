#definerer cars til 100
cars = 100
#definerer space_in_a_car til 4.0
space_in_a_car = 4.0
#def. drivers til 30
drivers = 30
#def. passengers til 90
passengers = 90
#def. cars_not_driven til regnestykket cars - drivers
cars_not_driven = cars - drivers
#def. cars_driven til antall førere
cars_driven = drivers
#def. carpool_capacity til antall ledige seter
carpool_capacity = cars_driven * space_in_a_car
# def average_passengers_per_car til gjennomsnittlig antall passasjerer 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
