"""Game - lab4, task 5"""
class Friend:
    """
    Empty class.
    """
    pass

class Person:
    """
    Empty class.
    """
    pass


class Enemy:
    """
    Class of enemy. Includes main usage of it.
    Functions:
    set_conversation
    set_weakness
    describe
    talk
    fight
    get_defeated
    """

    defeated = 0

    def __init__(self, enemy: str, description: str) -> None:
        """
        Initializes an enemy with its name and description.

        Parameters:
        enemy (str): The name of the enemy.
        description (str): The description of the enemy.
        """
        self.enemy = [enemy, description]
        self.description = description

    def set_conversation(self, conversation) -> None:
        """
        Adds conversation of the enemy.
        (2nd element od self.enemy)
        Example:
        >>> enemy = Enemy('Goblin', 'A nasty-looking goblin.')
        >>> enemy.set_conversation("I'll crush you like a bug!")
        >>> enemy.enemy[2]
        "I'll crush you like a bug!"
        """
        self.enemy.append(conversation)

    def set_weakness(self, weakness: str) -> None:
        """
        Adds enemy weakness.
        (3d element)
        Example:
        >>> enemy = Enemy('Goblin', 'A nasty-looking goblin.')
        >>> enemy.set_conversation("I'll crush you like a bug!")
        >>> enemy.set_weakness('sword')
        >>> enemy.enemy[3]
        'sword'
        """
        self.enemy.append(weakness)

    def describe(self) -> None:
        """
        Prints the name and description of the enemy.
        """
        print(f'{self.enemy[0]} is here!\n{self.enemy[1]}')

    def talk(self) -> None:
        """
        Prints the conversation of the enemy.
        """
        print(f'[{self.enemy[0]} says]: {self.enemy[2]}')

    def fight(self, item) -> bool:
        """
        Determines if the enemy is defeated or not.
        Example:
        >>> enemy = Enemy('Goblin', 'A nasty-looking goblin.')
        >>> enemy.set_conversation("I'll crush you like a bug!")
        >>> enemy.set_weakness('sword')
        >>> enemy.fight('sword')
        True
        >>> enemy.defeated
        1
        """
        if item == self.enemy[3]:
            Enemy.defeated += 1
            return True
        return False

    def get_defeated(self) -> int:
        """
        Returns the number of enemies defeated.
        """
        return Enemy.defeated


class Item:
    """
    Main class of items. Includes main information of it.
    Functions:
    set_description
    describe
    get_name
    """

    def __init__(self, item: str) -> None:
        """
        Initializes an item with its name.

        Parameters:
        item (str): The name of the item.
        """
        self.item = [item]

    def set_description(self, description: str) -> None:
        """
        Adds a description to an item.
        Example:
        >>> item = Item('sword')
        >>> item.set_description('A sharp and shiny sword.')
        >>> item.item[1]
        'A sharp and shiny sword.'
        """
        self.item.append(description)

    def describe(self) -> None:
        """
        Prints the name and description of the item.
        """
        print(f'The [{self.item[0]}] is here - {self.item[1]}')

    def get_name(self) -> str:
        """
        Returns the name of the item.
        """
        return self.item[0]


class Room:
    """
    Main class.
    Functions:
    set_description
    link_room
    set_character
    set_item
    get_character
    get_item
    move
    get_details
    """
    def __init__(self, room: str) -> None:
        """
        Initializes a room with its name.

        Parameters:
        room (str): The name of the room.
        """
        self.room = room
        self.name = str(room)
        self.description = ''
        self.linking = []
        self.character = None
        self.item = None
        self.defeated = 0


    def set_description(self, description: str) -> None:
        """
        Adds a description to a room.
        [room name, description of the room.]
        """
        self.description = description

    def link_room(self, next_room, part: str) -> None:
        """
        Adds information about the next room.
        Adds tuple.
        """
        self.linking.append((next_room, part))

    def set_character(self, enemy = Enemy) -> None:
        """
        Set the character (enemy) that is in this room.
        """
        self.character = enemy

    def set_item(self, item = Item) -> None:
        """
        Set the item that is in this room.
        """
        self.item = item

    def get_character(self):
        """
        Get the character (enemy) in this room.
        """
        if self.character is not None:
            return self.character
        return None

    def get_item(self):
        """
        Get the item in this room.
        """
        if self.item is not None:
            return self.item
        return None

    def move(self, move):
        """
        Move to another room.
        """
        for elem in self.linking:
            if elem[1] == move:
                self.room = elem[0]
        return self.room

    def get_details(self) -> None:
        """
        Print the details of the room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for elem in self.linking:
            print(f'The {elem[0].name} is {elem[1]}')


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
