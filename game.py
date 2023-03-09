class Enemy:
    
    def __init__(self, enemy: str, describtion: str) -> None:
        self.enemy = [enemy, describtion]

    def set_conversation(self, conversation) -> None:
        """
        Adding conversation of the enemy.
        (2 element)
        """
        self.enemy.append(conversation)

    def set_weakness(self, weakness: str) -> None:
        """
        Adding enemy weakness.
        (3d element)
        """
        self.enemy.append(weakness)

    def describe(self):
        print(f'{self.enemy[0]} is here!\n{self.enemy[1]}')


class Item:

    def __init__(self, item: str) -> None:
        self.item = [item]

    def set_description(self, description: str) -> None:
        """
        Adding description to an item.
        """
        self.item.append(description)

    def describe(self):
        print(f'The [{self.item[0]}] is here - {self.item[1]}')


class Player:
    pass

class Friend:
    pass

class Room:
    def __init__(self, room: str) -> None:
        self.room = [room]
        self.additional = []

    def __repr__(self) -> str:
        return self.room[0]

    def set_description(self, description: str) -> None:
        """
        Creating info about the room.
        [room name, description of the room.]
        """
        self.room.append(description)

    def link_room(self, next_room, part: str) -> None:
        """
        Adding information about the next room.
        """
        self.room.append((next_room, part))

    def set_character(self, enemy = Enemy) -> None:
        """
        Setting character to the room
        """
        self.additional.append(enemy)

    def set_item(self, item = Item):
        """
        Setting item to the room
        """
        self.additional.append(item)

    def get_character(self):
        for elem in self.additional:
            if isinstance(elem, Enemy):
                return elem
        return None

    def get_item(self):
        for elem in self.additional:
            if isinstance(elem, Item):
                return elem
        return None

    def move(self, move):
        for elem in self.room[2:]:
            if elem[1] == move:
                self.room = elem[0]

    def talk(self):
        pass

    def get_details(self) -> None:
        """
        Printing general details of the room.
        """
        print(self.room[0])
        print('--------------------')
        print(self.room[1])
        for elem in self.room[2:]:
            print(f'The {elem[0]} is {elem[1]}')


kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
kitchen.link_room(dining_hall, "south")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
kitchen.set_character(dave)
cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
kitchen.set_item(cheese)
kitchen.get_details()
inhabitant = kitchen.get_character()
inhabitant.describe()
item = kitchen.get_item()