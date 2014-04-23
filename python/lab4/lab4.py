

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = { 'student1': 'Marte Holen', \
'student2': 'Lisa Tvedt', \
            'student3': 'Mats Liver Skandsen', \
}

# Oppgave 1
# Funksjonen lager en strukturert utskrift av resultater fra
# kallet psutil.cpu_times().
# Modulen psutil må være installert.
#
# Utskriften skal være følgende (verdiene skal selvsagt være forskjellige):
# user = 3088.16
# nice = 0.99
# system = 897.37
# idle = 72353.81
# iowait = 19.29
# irq = 6.82
# softirq = 3.07
# steal = 0.00
# guest = 0.00
#
def psutils_use():
    """
Henter lister med systeminformasjon fra /proc og bearbeider disse
"""
    x = psutil.cpu_times()._fields
    y = psutil.cpu_times()
    r = zip(x, y)
    for name, value in r:
        print("\t%s = %s") % (name, value)

psutils_use()


# Oppgave 2
# Gitt følgende liste (inn-data):
# proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#
# skal funksjonen produsere følgende ut-data:
#
# C ble startet 1969 av Dennis Ritchie.
# C++ ble startet 1979 av Bjarne Stroustrup.
# Perl ble startet 1987 av Larry Wall.
# Python ble startet 1989 av Guido van Rossum.
# Java/Oak ble startet 1991 av James Gosling.
# Ruby ble startet 1991 av Yukihiro "Matz" Matsumoto.
# Go/golang ble startet 2007 av Robert Griesemer, Rob Pike, and Ken Thompson.
#
def print_history(proglangs):
# Implementer funksjonen her
    x = sorted(proglangs, key=lambda test: test[1]) #sorting the sexond variable, year.
    for z in x:
            print("%s ble startet %s av %s.") % (z[0], z[1], z[2])
    
    
proglangs = [('Python', '1989', 'Guido van Rossum'),
('C', '1969', 'Dennis Ritchie'),
('Java/Oak', '1991', 'James Gosling'),
('C++', '1979', 'Bjarne Stroustrup'),
('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'),
('Perl', '1987' , 'Larry Wall'),
('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]

print""
print_history(proglangs)


# Standardkall for evalueringen
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
if s is not "-":
print s
