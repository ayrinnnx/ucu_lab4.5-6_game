class Player:
    pass

class Friend:
    pass

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

    def talk(self):
        print(f'[{self.enemy[0]} says]: {self.enemy[2]}')

    def fight(self, item):
        return True if item == self.enemy[3] else False
    
    def get_defeated(self):
        pass


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

    def get_name(self):
        return self.item[0]


class Room:
    def __init__(self, room: str) -> None:
        self.room = room
        self.name = str(room)
        self.description = ''
        self.linking = []
        self.additional = [None, None]


    def set_description(self, description: str) -> None:
        """
        Creating info about the room.
        [room name, description of the room.]
        """
        self.description = description

    def link_room(self, next_room, part: str) -> None:
        """
        Adding information about the next room.
        """
        self.linking.append((next_room, part))

    def set_character(self, enemy = Enemy) -> None:
        """
        Setting character to the room
        """
        self.additional[0] = enemy

    def set_item(self, item = Item):
        """
        Setting item to the room
        """
        self.additional[1] = item

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
        for elem in self.linking:
            if elem[1] == move:
                self.room = elem[0]
                self.name = elem[0].name
                self.description = elem[0].description
                self.linking = elem[0].linking
        return self.room

    def get_details(self) -> None:
        """
        Printing general details of the room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for elem in self.linking:
            print(f'The {elem[0].name} is {elem[1]}')


# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")
# dining_hall = Room("Dining Hall")
# dining_hall.set_description("A large room with ornate golden decorations on each wall.")
# kitchen.link_room(dining_hall, "south")

# dave = Enemy("Dave", "A smelly zombie")
# dave.set_conversation("What's up, dude! I'm hungry.")
# dave.set_weakness("cheese")
# kitchen.set_character(dave)
# cheese = Item("cheese")
# cheese.set_description("A large and smelly block of cheese")
# kitchen.set_item(cheese)
# kitchen.get_details()
# inhabitant = kitchen.get_character()
# inhabitant.describe()
# inhabitant.talk()
# item = kitchen.get_item()