#Using for loop

# def badge_maker(name):
#     return 'Hello, my name is %s.' % name
# badge_maker('Arel')

# def batch_badge_creator(names):
#     badge_msgs = []
#     for name in names:
#         badge_msgs.append(badge_maker(name))
#     return badge_msgs
# batch_badge_creator(['Arel','Carol'])
    

# def assign_rooms(names):
#     room_assign= []
#     for room in range(len(names)):
#         room_no = room + 1
#         room_assign.append('Hello, %s! You\'ll be assigned to room %s!' % (names[room], room_no))
#     return room_assign
# assign_rooms(['Arel','Carol'])

# def printer(names):
#     badge_msg = []
#     for name in names:
#         badge_msg.append("Hello, my name is %s." % name)
#     for room, name in enumerate(names):
#         room_no = room + 1
#         room_assign = "Hello, %s! You'll be assigned to room %s!" % (name, room_no)
#         badge_msg.append(room_assign)
#     return "\n".join(badge_msg)

# printer(["Arel", "Carol"])



#Using list comprehension

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]
batch_badge_creator (['Arel','Carol'])

def assign_rooms(names):
    return ['Hello, %s! You\'ll be assigned to room %s!' % (name, room) for room, name in enumerate(names, start= 1)]
assign_rooms(['Arel','Carol'])

def printer(names):
    badges = [f"Hello, my name is {name}." for name in names]
    room_assignments = [f"Hello, {name}! You'll be assigned to room {room+1}!" for room, name in enumerate(names)]

    for badge in badges:
        print(badge)
    for room_assignment in room_assignments:
        print(room_assignment)

printer(["Arel", "Carol"])