import random
def create_deck():
    deck = {
        'Ace of Spades':1,
        '2 of Spades':2,
        '3 of Spades':3,
        '4 of Spades':4,
        '5 of Spades':5,
        '6 of Spades':6,
        '7 of Spades':7,
        '8 of Spades':8,
        '9 of Spades':9,
        '10 of Spades':10,
        'Jack of Spades':10,
        'Queen of Spades':10,
        'King of Spades':10,

        'Ace of Hearts':1,
        '2 of Hearts':2,
        '3 of Hearts':3,
        '4 of Hearts':4,
        '5 of Hearts':5,
        '6 of Hearts':6,
        '7 of Hearts':7,
        '8 of Hearts':8,
        '9 of Hearts':9,
        '10 of Hearts':10,
        'Jack of Hearts':10,
        'Queen of Hearts':10,
        'King of Hearts':10,
        
        'Ace of Clubs':1,
        '2 of Clubs':2,
        '3 of Clubs':3,
        '4 of Clubs':4,
        '5 of Clubs':5,
        '6 of Clubs':6,
        '7 of Clubs':7,
        '8 of Clubs':8,
        '9 of Clubs':9,
        '10 of Clubs':10,
        'Jack of Clubs':10,
        'Queen of Clubs':10,
        'King of Clubs':10,
        
        'Ace of Diamonds':1,
        '2 of Diamonds':2,
        '3 of Diamonds':3,
        '4 of Diamonds':4,
        '5 of Diamonds':5,
        '6 of Diamonds':6,
        '7 of Diamonds':7,
        '8 of Diamonds':8,
        '9 of Diamonds':9,
        '10 of Diamonds':10,
        'Jack of Diamonds':10,
        'Queen of Diamonds':10,
        'King of Diamonds':10,
    }
    return deck #returns the deck

def deal_card(deck):
    cards= []
    card = random.choice(list(deck.items()))
    del deck[card[0]]
    cards.append(card)
    return card

def calculate_hand(hand):
    total = 0
    num_aces =0
    for card in hand:
        value = card[1]
        if value == 1:
            num_aces +=1
        total+= value
    while num_aces > 0 and total + 10 <=21:
        total += 10
        num_aces -= 1
    return total

def main():
    deck = create_deck() 
    player1_hand = [deal_card(deck) for i in range(2)]
    player2_hand = [deal_card(deck) for i in range(2)]
    print(f'Player 1 hand: {player1_hand}')
    print(f'Player 2 hand: {player2_hand}')
    player1_total = calculate_hand(player1_hand)
    while player1_total < 17:
        player1_hand.append(deal_card(deck))
        player1_total = calculate_hand(player1_hand)
        print('Player 1 hits')
        print(f'Player 1 hand: {player1_hand}')
    if player1_total > 21:
        print('Player 1 busts!')
    else:
        print('Player 1 stands')
    player2_total = calculate_hand(player2_hand)
    while player2_total < 17:
        player2_hand.append(deal_card(deck))
        player2_total = calculate_hand(player1_hand)
        print('Player 2 hits')
        print(f'Player 2 hand: {player1_hand}')
    if player2_total > 21:
        print('Player 2 busts!')
    else:
        print('Player 2 stands')

    if player1_total > 21:
        print('Player 2 wins')
    elif player2_total > 21:
        print('Player 1 wins')
    elif player1_total > player2_total:
        print('Player 1 wins')
    elif player2_total > player1_total:
        print('Player 2 wins')
    else:
        print('It is a tie')

if __name__ == '__main__':
    main()