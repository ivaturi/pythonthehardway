
# Room model

# A room has the following properties:
#    - Connections to other rooms
#    -
room_list = {
    "corridor" : "Main Corridor",
    "storage"  : "Storage",
    "closet"   : "Walk-in Closet",
    "bath"     : "Bathroom",
    "kitchen"  : "Kitchen",
    "guest"    : "Guest Bedroom",
    "hall"     : "Living Room",
    "bedroom"  : "Main Bedroom",
    "balcony"  : "Balcony"
}



class Room:
    """
    The base class for rooms
    """
    
    def __init__(self,name):
        """
        Create a room
        """
        self.__name = name
        self.__connections = {}

    def connections(self):
        """
        Returns the connections that are configured for this room.
        """
        return self.__connections

    def connectTo(self, *rooms):
        """
        Defines connections for the room.
        Accepts keys from room_list
        """
        for room in rooms:
            if room in room_list:
                self.__connections[room] = room_list[room]
            else:
                pass    
