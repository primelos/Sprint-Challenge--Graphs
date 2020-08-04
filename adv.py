from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"  #20 moves
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"  #996 moves

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
print('top',traversal_path)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# directions N,S,W,E
# return opposite of current direction.(move)
# EXAMPLE - if move is "north" then return "south".

def exit(direct):
    if direct == "n":
        return "s"
    if direct == "s":
        return "n"
    if direct == "w":
        return "e"
    if direct == "e":
        return "w"
# print('room',room_graph[0][1])
def dft_traversal(traversal_path):

    visited = set()
    ss = Stack()
    ss.push(0)

    #while length of rooms visited is less than length of total rooms.
    # print('1',len(visited))
    # print('2',len(room_graph))
    while len(visited) < len(room_graph):

        current_room = ss.stack[-1]
        visited.add(current_room) #add current room to set
        next_room = room_graph[current_room][1]
        # print('next_room', next_room)
        not_visited = [] # empty array/list

        # print(f"CURRENT ROOM: {current_room}")
        
        for move, room in next_room.items(): # move in direction of room in next_room
            # print('move',move)
            # print('room', room)
            if room not in visited: #if room is not in visited rooms
                not_visited.append((room, move))  # add room and move 
                print('not_visited', not_visited)
        if len(not_visited) > 0: #if length of not visited greater than 0
            ss.push(not_visited[0][0]) #add not_visited onto stack, room, move
            print(not_visited[0][0])
            traversal_path.append(not_visited[0][1]) #attach not visited to traversal path, room. direction plus 1?
            print('1',not_visited[0][1])

        else:
            ss.pop() #remove from stack
            
            for move, room in next_room.items():
                # print('move2',move)
                # print('room2', room)
                if room == ss.stack[-1]: # if room value is equal to value of stack
                    traversal_path.append(move) # get traversal and add direction

    print('before', traversal_path)
    traversal_path.pop() #remove last move from traversal
    print('after', traversal_path)




dft_traversal(traversal_path)

print('traversal_path',traversal_path)













# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
