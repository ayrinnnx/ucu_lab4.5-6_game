"""Main.py"""
import game

player = game.Person(input("Введи ім'я: "))
player.set_lives(2)
print(player)

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

rynok.link_room(square, "північ")
square.link_room(rynok, "південь")
square.link_room(street, "схід")
square.link_room(kfc, "захід")
kfc.link_room(opera, "північ")
opera.link_room(vernisaz, "схід")
street.link_room(vernisaz, "захід")
vernisaz.link_room(square, "південь")


granny = game.Boss("Гадра", "Сварлива бабця, що йде по твою душу.")  #boss
granny.set_conversation("Внучок/внученька, ходь до мене побалакати.")
granny.set_weakness("Пиріжок")
granny.set_weakness_command('говорити')
granny.set_add_hearts(1)
street.set_character(granny)

helper = game.Friend("Заволока", "Бродяга, що має багато цікавих дрібничок на допомогу.")
helper.set_conversation("...цікавий я сувенірчик недавно знайшов...")
opera.set_character(helper)

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
food.set_description("А пахне то як!!")
kfc.set_item(food)

ex = game.Item("Сокира")
ex.set_description("Штучка, щоб іти по головах.")
square.set_item(ex)

cucumber = game.Item("Квашений огірок")
cucumber.set_description("Солененький такий, ммм...")
street.set_item(cucumber)

sleep = game.Item("Снодійне")
sleep.set_description("Дві пілюлі і спиш як вбитий.")
rynok.set_item(sleep)

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

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif inhabitant is not None and inhabitant.get_name() == 'Гадра' and command == granny.boss_special[0]:
        if granny.boss_special[1] == 1:
            granny.boss_special[1] = 'x'
            print('Вона почувається тепер краще і хоче менше заподіяти шкоди.')
        else:
            try:
                granny.boss_special[1] -= 1
                print('Вона почувається тепер краще і хоче менше заподіяти шкоди.')
            except TypeError:
                print('Забагато говориш, вона злиться вже!!')
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant.get_name() == 'Заволока' and inhabitant.speech() and player.lives < 3:
                hearts = game.Hospital("Сердечкиии")
                hearts.set_description("Додаткове життя.")
                opera.set_item(hearts)

    elif command == "битися":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("З чим битимешся?")
            print("Твій рюкзак:  ", backpack)
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.get_name() != 'Заволока' and inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    if (inhabitant.get_name() == 'Гадра' and granny.boss_special[1] == 'x') or inhabitant.get_name() != 'Гадра':
                        print("Йоу, ти виграв!")
                        current_room.character = None
                    elif inhabitant == granny:
                        print("Мінус одне життя в бабуськи!!")
                    if inhabitant.get_defeated() == 4:
                        print("Ну що ж, ти вижив серед прогулянки. Молодець!")
                        dead = True
                elif inhabitant.get_name() == 'Заволока':
                    print("Не бий мене!!!")
                else:
                    # What happens if you lose?
                    print("Ти програв битву.")
                    if player.check_lives():
                        print(f'Ти досі маєш шанс на перемогу, бо твоєї смерті ще {player.lives} ударів.')
                    else:
                        print("Тобі прийшов кінець.")
                        dead = True
            else:
                print("Ти не маєш " + fight_with)
        else:
            print("Нема з ким битися")
    elif command == "взяти":
        if item.get_name() == 'Сердечкиии':
            hearts.get_more_hearts()
            print(hearts)
            print(f'У тебе ще стільки ударів до смерті: {player.lives}\n')
            current_room.set_item(None)
        elif item is not None:
            print("Ти помістив " + item.get_name() + " до рюкзака")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Нема що взяти!")
    else:
        print("Я не знаю як " + command)
