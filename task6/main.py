"""Main.py"""
import game

rynok = game.Room("Стрийський ринок")
rynok.set_description("Ринок пригод.")

square = game.Room("Площа Ринок")
square.set_description("Місце, де можуть розвести на грошики.")

street = game.Room("Підвальна")
street.set_description("Дивна вулиця.")

kfc = game.Room("KFC")
kfc.set_description("...смажені крильця.")

opera = game.Room("Львівська опера")
opera.set_description("Опера, опера, опера.....")

vernisaz = game.Room("Вернісаж")
vernisaz.set_description("Барахолочка дивних речей.")

rynok.link_room(square, "north")
square.link_room(rynok, "south")
square.link_room(street, "east")
square.link_room(kfc, "west")
kfc.link_room(opera, "north")
opera.link_room(vernisaz, "east")
street.link_room(vernisaz, "west")
vernisaz.link_room(square, "south")


granny = game.Boss("Гадра", "Сварлива бабця, що йде по твою душу.")  #boss
granny.set_conversation("Внучок/внученька, ходь до мене побалакати.")
granny.set_weakness("Сокира")
granny.set_weakness_command('talk')
granny.set_add_hearts(1)
rynok.set_character(granny)

buhach = game.Enemy("Бухач", "Злодій, який готовий обікрати тебе за кутом.")
buhach.set_conversation("Не бійся, я не страшний, нічого не зроблю.")
buhach.set_weakness("Сокира")
vernisaz.set_character(buhach)

habal = game.Enemy("Хабаль", "Залицяльник, що краде твій час.")
habal.set_conversation("Зіронька моя, постій зі мною...")
habal.set_weakness("Снодійне")
square.set_character(habal)

hirus = game.Enemy("Хірус", "Прекрасний пияка, що готовий розділити з тобою бутилку на двох.")
hirus.set_conversation("Сьогодні свято, пішли пити.")
hirus.set_weakness("Квашений огірок")
kfc.set_character(hirus)

food = game.Item("Пиріжок")
food.set_description("A large and smelly block of cheese")
kfc.set_item(food)

ex = game.Item("Сокира")
ex.set_description("A really good book entitled 'Knitting for dummies'")
rynok.set_item(ex)

cucumber = game.Item("Квашений огірок")
cucumber.set_description("A large and smelly block of cheese")
street.set_item(cucumber)

sleep = game.Item("Снодійне")
sleep.set_description("A really good book entitled 'Knitting for dummies'")
opera.set_item(sleep)

current_room = rynok
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif inhabitant.get_name() == 'Гадра' and command == granny.boss_special[0]:
        if granny.boss_special[1] == 1:
            granny.boss_special[1] = 'x'
            print('You made her better. Now she has one less heart of life.')
        else:
            try:
                granny.boss_special[1] -= 1
                print('You made her better. Now she has one less heart of life.')
            except TypeError:
                print('You speak too much!!')
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    if (inhabitant.get_name() == 'Гадра' and granny.boss_special[1] == 'x') or inhabitant.get_name() != 'Гадра':
                        print("Hooray, you won the fight!")
                    elif inhabitant == granny:
                        print("Your granny has one heart less. Try smth else, too!!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 4:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
