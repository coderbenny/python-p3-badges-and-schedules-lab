def badge_maker(name):
    return f"Hello, my name is {name}."

print(badge_maker("Benny"))

def batch_badge_creator(names):
    badges = ['Hello, my name is ' + item + '.' for item in names]
    return badges        

print(batch_badge_creator(["Arel","Carol"]))

def assign_rooms(names):
    rooms = range(1, len(names) + 1)
    return [f"Hello, {name}! You'll be assigned to room {room}!" for room, name in enumerate(names, start = 1)]

print(assign_rooms(["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George"]))

def printer(names):
    badges = batch_badge_creator(names)
    room_assignment = assign_rooms(names)

    for item in badges:
        print(item)

    for room in room_assignment:
        print(room)

printer(["Arel", "Carol"])
