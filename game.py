class Room:
    def __init__(self, room: str) -> None:
        self.room = [room]

    def __repr__(self) -> str:
        return self.room[0]

    def set_description(self, description: str) -> list:
        """
        Creating info about the room.
        [room name, description of the room.]
        """
        self.room.append(description)

    def link_room(self, next_room, part: str) -> list:
        """
        Adding information about the next room.
        """
        self.room.append((next_room, part))

    def get_character(self):
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

# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")
# dining_hall = Room("Dining Hall")
# dining_hall.set_description("A large room with ornate golden decorations on each wall.")
# kitchen.link_room(dining_hall, "south")
# kitchen.get_details()

class Enemy:
    pass

class Item:
    def __init__(self, item: str) -> None:
        self.item = item

    def set_description(self, description: str) -> str:
        #smth with description
        pass

class Player:
    pass

class Friend:
    pass
