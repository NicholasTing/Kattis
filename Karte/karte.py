data = input()

card = ""
cards = []

P = ["P01","P02","P03","P04","P05","P06","P07","P08","P09","P10","P11","P12","P13"]
K = ["K01","K02","K03","K04","K05","K06","K07","K08","K09","K10","K11","K12","K13"]
H = ["H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13"]
T = ["T01","T02","T03","T04","T05","T06","T07","T08","T09","T10","T11","T12","T13"]

suits = [P,K,H,T]

greska = False
newCard = 1

for letter in data:

    if letter.isalpha():
        if newCard:
            card += (letter)
            newCard = 0
        else:
            if card in cards:
                greska = True

            cards.append(card)

            for suit in suits:
                if card in suit:
                    suit.remove(card)
                    

            card = ""
            card += (letter)

    elif letter.isdigit():
        card +=(letter)

if card in cards:
    greska = True

cards.append(card)

for suit in suits:
    if card in suit:
        suit.remove(card)


if greska:
    print("GRESKA")

else:
    print(str(len(P)) + " " + str(len(K)) + " " + str(len(H)) + " " + str(len(T)))
