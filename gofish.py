import random
deck=['Ace of Clubs','Two of Clubs','Three of Clubs','Four of Clubs','Five of Clubs', 'Six of Clubs','Seven of Clubs','Eight of Clubs','Nine of Clubs','Ten of Clubs','Jack of Clubs','Queen of Clubs','King of Clubs',
    'Ace of Diamonds','Two of Diamonds','Three of Diamonds','Four of Diamonds','Five of Diamonds','Six of Diamonds','Seven of Diamonds','Eight of Diamonds','Nine of Diamonds','Ten of Diamonds','Jack of Diamods','Queen of Diamonds','King of diamonds',
    'Ace of Hearts','Two of Hearts','Three of Hearts','Four of Hearts','Five of Hearts','Six of Hearts','Seven of Hearts','Eight of Hearts','Nine of Hearts','Ten of Hearts','Jack of Hearts','Queen of Hearts','King of Hearts',
    'Ace of Spaids','Two of Spaids','Three of Spaids','Four of Spaids','Five of Spaids','Six of Spaids','Seven of Spaids,','Eight of Spaids','Nine of Spaids','Ten of Spaids','Jack of Spaids','Queen of Spaids','King of Spaids']
    #the deck of cards
numscanask=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    #list of numbers you or the comptuer can ask for
yourask=None
computerask=None
count=int(0) #count for picking the cards
def menu():
    gametype=input("Press 1 For Singleplayer or 2 for Multiplayer")
    
    if gametype==1:
        singleplayer()
    if gametype==2:
        multiplayer()
    else:
        print("invalid choice")
        menu()

def singleplayer():
    yourhand=[]
    global count
    global yourask
    global count
    global numscanask
    while count<7:
        cardpick=random.randrange(0,len(deck))
        card=deck[cardpick]
        yourhand.append (card)
        deck.remove(card)
        count+=1
    count=0
    while count<7:
        cardpick=random.randrange(0,len(deck))
        card=deck[cardpick]
        computerhand.append (card)
        deck.remove(card)
        count+=1
    print (yourhand)
    print (computerhand)
    

    yourask=int(input("What card Do you want a pair of(enter 11 for jack, 12 for queen or 13 for king)"))
    yourask-=1
    yournumber=numscanask[yourask]
    for card in computerhand:
        if card == yournumber:
            print("yay")
            break
        #do something like this
    if yournumber in computerhand[0] or computerhand[1] or computerhand[2] or computerhand[3] or computerhand[4] or computerhand[5] or computerhand[6] or computerhand[7]:
      print("this loop works")
    else:
        print("nope")
    #you could also use something along these lines for card picking
        computerhand= random.shuffle(deck)[0:7]



   
singleplayer()