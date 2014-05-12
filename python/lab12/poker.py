# -*- coding: latin-1 -*-

#
#  IS-105 LAB11
#  Implementer alt som er markert med OPPGAVE.
#  I tillegg skal du i filen lab11defs.txt beskrive et program (så detaljert du kan)
#	for en poker server, hvor spillere kan melde seg på et poker spill, 
#	få utdelt en hånd hver, legge inn en sats eller kaste sin hånd 
#	og få utpekt en (eller flere i tilfelle uavgjort) vinner.
#	Det er lagt ut flere implementasjoner av sockets klient-tjener modell i Class Fronter.
#	Det som er aktuelt å se på er de som er implementert i Python.
#
#  lab11.py - kildekode som inneholder studentenes løsning.
#         
#
#
import random # brukes for å dele ut kort

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Marte Holen', \
			'student2': 'Lisa Tvedt', \
            'student3': 'Mats Liver Skandsen', \
}

# Oppgave 
# 	Implementere pokerspill. Vi begynner med representasjon og testing.
#
#	Testing i Python kan gjøres med assert. Eksemplet under skal være selvforklarende.
#
#   Det er gitt et kortstokk http://en.wikipedia.org/wiki/Playing_card med 52 kort.
#	I denne oppgaven prøver vi å lage et prototype som gir svar på følgende:
#	Hvordan representere alle kort? Hvordan finne ut hvilken hånd er best? Hvordan dele ut kort?
#
#   Les deg opp på hva poker er og hvordan det spilles, hvis du ikke kjenner til det fra før.
#	Domenkunnskap i systemutvikling er viktigst!!!
#	http://no.wikipedia.org/wiki/Poker
#	http://en.wikipedia.org/wiki/Poker
#
#	Her er et forslag for representasjon av kort og hender, som jeg anbefaler dere å bruke.
#	Dere kan gjøre egne modifikasjoner, med de må være begrunnet i lab11defs.txt filen.
#
#   Typer (kind): H - heart, S - spade, C - club, D - diamond (13 kort av hver type)
#   Verdi (rank): A - ace, K - king, Q - queen, J - jack, T - ten, 9, 8, 7, 6, 5, 4, 3, 2
#   En hånd (hand): består av 5 kort http://en.wikipedia.org/wiki/Hand_rankings
#   Hånd rangeres fra høyest til lavest (i paranteser anbefalt navn på variabelen på en hånd): 
#		 8 - Straight flush (sf) (finnes også Royal Flush, som er den beste av Straight flush)
#		 7 - Four of a Kind (fk) 
#		 6 - Full House (fh) 
#	     5 - Flush (fl)
#		 4 - Straight (st) 
#		 3 - Three of a kind (tk) 
#	     2 - Two Pair (tp) 
#        1 - One Pair (op) 
#        0 - High Card (hc)
#   
#
# OPPGAVE: erstatt max med en funksjon allmax, som tar hensyn til uavgjort mellom to eller flere hender 
def poker(hands):
	"""
		Denne funksjonene må omdefineres for å ta hensyn til spesialtilfelle med flere like "Straight Flush" hender
		dvs. uavgjort
		Returnerer en eller flere hender: poker([hand, ...]) => [[hand], ...]
		hand_rank er en funksjon som må skrives og brukes i sammenligningen av "hender"
	"""
	return allmax(hands, key=hand_rank)

	
# OPPGAVE: fullføre denne funksjonene for alle hender i poker og lage tester med assert
def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) 
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks)) # 99993 (7,9,3)
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks) and kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(hand):
        return (4, ranks)
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return hand 
	
# Funksjonene card_ranks(hand) returnerer en ORDNET (sorted) tuple av verdier (ranks)
# Verdier for J, Q, K og A er tilsvarende 11, 12, 13, 14. 
# En hånd TD TC TH 7C 7D skal returnere [10,10,10,7,7]
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

# OPPGAVE: Implementer denne funksjonen
# Funksjonen straight(ranks) returner True hvis hånden er en Straight.
def straight(ranks):

	if max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5:
		return True
	else:
		return False

# OPPGAVE: Implementere denne funksjonen
# Funksjonen flush(hand) returnerer True hvis hånden er en Flush.
def flush(hand):
	types = [t for v,t in hand]
	if len(set(types)) == 1:
		return True
	else:
		return False

# OPPGAVE: Implementer denne funksjonen
# Funksjonen kind(nr, ranks) returnerer den første verdien (rank) som hånden har nøyaktig n av.
# For en hånd med 4 syvere, skal denne funksjonen returnere 7.
def kind(nr, ranks):
	for r in ranks:
		if ranks.count(r) == nr: return r
	return None

# OPPGAVE: Implementer denne funksjonen
# Funksjonen two_pair(ranks) gjør følgende:
# hvis det er Two Pair, skal funksjonen returnere deres verdi (rank) som en tuple.
# For eksempel, en hånd med to toere og 2 firere vil gi en returverdi på (4, 2).
def two_pair(ranks):
	pair = kind(2, ranks)
	lowpair = kind(2, list(reversed(ranks)))
	if pair and lowpair != pair:
		return (pair, lowpair)
	else:
		return None

# OPPGAVE: Implementer denne funksjonen (brukes i poker funksjonen for å løse uavgjort tilfeller)
# For eksempel, gitt 4 følgende hender
#   [['6C', '7C', '8C', '9C', 'TC'],
#   ['6D', '7D', '8D', '9D', 'TD'],
#   ['9D', '9H', '9S', '9C', '7D'],
#   ['TD', 'TC', 'TH', '7C', '7D']]
# skal allmax returnere to hender [['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD']]
def allmax(iterable, key=None):
		result, maxval = [], None
		key = key or (lambda x: x)
		for x in iterable:
			xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
		elif xval == maxval:
			result.append(x)
    		return result


# Denne strukturen definerer et kortstokk for poker
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

# Denne funksjonen deler ut numhands med n kort i hver hånd
def deal(numhands, n=5, deck=mydeck):
    # Your code here.
	random.shuffle(deck)
	return [deck[n*i:n*(i+1)] for i in range(numhands)]





