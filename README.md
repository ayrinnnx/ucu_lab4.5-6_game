# task5

Creating a game.py file based on this main.py module. A game that involves fighting monsters in the terminal. Consists of 3 rooms (Ballroom, Kitchen, Dining_hall), two monsters (Tabita, Dave) and two items (cheese, book).

Main methods: 'fight', 'talk', 'take' and moving ('west', 'east', 'north', 'south').

Game continues till all 2 monsters are not killed.

Implemented 3 classes:
- Item (Functions:
    set_description,
    describe,
    get_name)
- Enemy (Functions:
    set_conversation,
    set_weakness,
    describe,
    talk,
    fight,
    get_defeated)
- Room (Functions:
    set_description,
    link_room,
    set_character,
    set_item,
    get_character,
    get_item,
    move,
    get_details)
    
Example of usage in log.txt (was provided with the task). No additional functions.

# task6

Similar to previous one, but a game throw Lviv. Consists of 6 places (KFC, Stryi market, Market Square, Podvalna street, Lviv Opera, Vernissage), three monsters (Бухач, Хабаль, Хірус), a boss (Гадра), a helper (Заволока) and four items (Пиріжок, Сокира, Квашений огірок, Снодійне). Each enemy has its own element that needs to be 'killed'. The game is played in Ukrainian. Added four more classes: Person, Boss, Friend, Hospital.

Main methods: 'говорити', 'битися', 'взяти' and moving ('північ', 'південь', 'захід', 'схід')

The rules of the game are slightly changed, namely:
- from the beginning the player has two lives
- the player can talk to a friend if he understands who it is
- the player has the opportunity to gain one extra life
- the boss battle requires two actions
- the player sees everything in the backpack before the battle


Example of game process:
![Screenshot 2023-03-14 005839](https://user-images.githubusercontent.com/117468608/224850943-568c67ab-bdb7-4790-a2cf-535b2efe42b0.png)


Additional information about how to win:
- a friend -> "Заволока" (need to speak with him and tell him a joke with length more than 10 symbols) at Lviv Opera
- methods of killing and main info:

-- "Гадра" (boss) at Podvalna street needs 'говорити' and 'Пиріжок'

-- "Бухач" at Vernissage needs "Сокира"

-- "Хабаль" (boss) at Market Square needs 'Снодійне'

-- "Хірус" at KFC needs "Квашений огірок"
