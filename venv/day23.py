import random

hallway = ['.']*11
room_1 = [2,'D', 'B']
room_2 = [4,'D', 'A']
room_3 = [6,'C', 'B']
room_4 = [8,'C', 'A']

def energy(amphipods):
    if amphipods == 'A':
        return 1
    elif amphipods == 'B':
        return 10
    elif amphipods =='C':
        return 100
    else:
        return 1000

def available_hallway_spots(hallway, room, position_in_room):
    hallway_spots_with_amphipods = [ind for ind, i in enumerate(hallway) if i!='.']
    all_spots = [0, 1, 3, 5, 7, 9, 10]
    #print(hallway_spots_with_amphipods)
    if hallway_spots_with_amphipods==[] and (position_in_room == 1 or (position_in_room == 2 and room[1]=='.')):
        return all_spots
    elif hallway_spots_with_amphipods!=[] and (position_in_room == 1 or (position_in_room == 2 and room[1]=='.')):
        less_than_room = 0 if [i for i in hallway_spots_with_amphipods if i<room[0]]==[] else max([i for i in hallway_spots_with_amphipods if i<room[0]])+1
        more_than_room = 11 if [i for i in hallway_spots_with_amphipods if i>room[0]] ==[] else min([i for i in hallway_spots_with_amphipods if i>room[0]])
        return list(set(range(less_than_room, more_than_room)).intersection(set(all_spots)))
    else:
        return []

def target_room(amphipods):
    global room_1, room_2, room_3, room_4
    if amphipods == 'A':
        return room_1
    elif amphipods == 'B':
        return room_2
    elif amphipods == 'C':
        return room_3
    else:
        return room_4

def go_to_room_from_room(hallway, room, position_in_room):
    global room_1, room_2, room_3, room_4
    targetRoom = target_room(room[position_in_room])
    av_spots = available_hallway_spots(hallway, room, position_in_room)
    value = 0
    if targetRoom == room:
        return 0, value
    else:
        if targetRoom[0] in range(min(av_spots)-2, max(av_spots)+2):
            if targetRoom[1:] == ['.', '.']:
                value = (2+(1 if position_in_room==2 else 0)+abs(targetRoom[0]-room[0])+1)*energy(room[position_in_room])
                targetRoom[2] = room[position_in_room]
                room[position_in_room] = '.'
                return 1, value
            elif targetRoom[1:] == ['.', room[position_in_room]]:
                value = (1 + (1 if position_in_room == 2 else 0) + abs(targetRoom[0] - room[0])+1 )*energy(room[position_in_room])
                targetRoom[1] = room[position_in_room]
                room[position_in_room] = '.'
                return 1, value
            else:
                return 0, value
        else:
            return 0, value

def go_to_room_from_hallway(hall, position):
    global room_1, room_2, room_3, room_4, hallway
    targetRoom = target_room(hall[position])
    hallway_spots_with_amphipods = [ind for ind, i in enumerate(hall) if i != '.']
    less_than_position = 0 if [i for i in hallway_spots_with_amphipods if i < position] == [] else max(
        [i for i in hallway_spots_with_amphipods if i < position]) + 1
    more_than_position = 11 if [i for i in hallway_spots_with_amphipods if i > position] == [] else min(
        [i for i in hallway_spots_with_amphipods if i > position])
    av_spots = list(range(less_than_position, more_than_position))
    value = 0
    if targetRoom[0] in range(min(av_spots)-1, max(av_spots)+2):
        if targetRoom[1:] == ['.', '.']:
            value = (2 + abs(targetRoom[0] - position) ) *energy(hall[position])
            targetRoom[2] = hall[position]
            hallway[position] = '.'
            return 1, value
        elif targetRoom[1:] == ['.', hall[position]]:
            value = (1 + abs(targetRoom[0] - position))* energy(hall[position])
            targetRoom[1] = hall[position]
            hallway[position] = '.'
            return 1, value
        else:
            return 0, value
    else:
        return 0, value


#print(available_hallway_spots(hallway, room_3, 1))
#print(go_to_room_from_room(['A', 'A', '.', '.', '.', '.', '.', '.', '.', 'B', 'A'], room_1, 1))
#print(go_to_room_from_hallway(['A', 'A', '.', '.', '.', 'D', '.', 'C', '.', 'B', 'A'], 5))
value_max = 16127
step= 0


value_max = 30000
for g in range(0,100000):
    cont = 1
    value = 0
    hallway = ['.'] * 11
    room_1 = [2, 'D', 'B']
    room_2 = [4, 'D', 'A']
    room_3 = [6, 'C', 'B']
    room_4 = [8, 'C', 'A']
    while (room_1[1:]!=['A', 'A'] or room_2[1:]!=['B', 'B'] or room_3[1:]!=['C', 'C'] or room_4[1:]!=['D', 'D']) and cont==1: #and \
            #len([ind for ind, i in enumerate(hallway) if i != '.'])<5:

        c1 = 0
        for h in [ind for ind, i in enumerate(hallway) if i != '.']:
            outcome = go_to_room_from_hallway(hallway, h)
            if outcome[0] == 1:
                c1 += 1
                value += outcome[1]
        c2 = 0
        still_has_av_spots = []
        for h in [room_1, room_2, room_3, room_4]:
            if h[1]!='.':
                try:
                    outcome = go_to_room_from_room(hallway, h, 1)
                    if outcome[0] == 1:
                        c2 += 1
                        value += outcome[1]
                except:
                    pass
                try:
                    av_spots = available_hallway_spots(hallway, h, 1)
                    c2 += 1 if len(av_spots) > 0  else 0
                    if len(av_spots)>0:
                        still_has_av_spots.append(h)
                except:
                    pass
            elif h[2]!='.':
                try:
                    outcome = go_to_room_from_room(hallway, h, 2)
                    if outcome[0] == 1:
                        c2 += 1
                        value += outcome[1]
                except:
                    pass
                try:
                    av_spots = available_hallway_spots(hallway, h, 2)
                    c2 += 1 if len(av_spots) > 0  else 0
                    if len(av_spots) > 0:
                        still_has_av_spots.append(h)
                except:
                    pass
        c3 = [sublist for sublist in still_has_av_spots if sublist != [2, 'A', 'A'] \
                     and sublist != [4, 'B', 'B'] and sublist != [6, 'C', 'C'] and sublist != [8, 'D', 'D'] \
                     and sublist != [2, '.', 'A'] \
                     and sublist != [4, '.', 'B'] and sublist != [6, '.', 'C'] and sublist != [8, '.', 'D'] \
                     and sublist != [2, '.', '.'] \
                     and sublist != [4, '.', '.'] and sublist != [6, '.', '.'] and sublist != [8, '.', '.']]
        cont = 0 if max(c1, c2)==0 or len(c3)==0 else 1
        if cont==0:
            for h in [ind for ind, i in enumerate(hallway) if i != '.']:
                outcome = go_to_room_from_hallway(hallway, h)
                if outcome[0] == 1:
                    c1 += 1
                    value += outcome[1]
        try:
            random_location = []
            random_location = random.choice(
                    [sublist for sublist in still_has_av_spots if sublist != [2, 'A', 'A'] \
                     and sublist != [4, 'B', 'B'] and sublist != [6, 'C', 'C'] and sublist != [8, 'D', 'D'] \
                     and sublist != [2, '.', 'A'] \
                     and sublist != [4, '.', 'B'] and sublist != [6, '.', 'C'] and sublist != [8, '.', 'D'] \
                     and sublist != [2, '.', '.'] \
                     and sublist != [4, '.', '.'] and sublist != [6, '.', '.'] and sublist != [8, '.', '.']])
            positions = [ind for ind, k in enumerate(random_location) if k != '.' and not str(k).isdigit()]

            random_position = random.choice(positions)
            if len(random_location)==3:
                try:
                    outcome = go_to_room_from_room(hallway, random_location, random_position)
                    if outcome[0] == 1:
                        step += 1
                        value += outcome[1]
                        #print(random_location[random_position], value)
                except:
                    outcome = (0,0)
                if outcome[0] == 0:
                    try:
                        av_spots = available_hallway_spots(hallway, random_location, random_position)
                        random_av_spot = random.choice(av_spots)
                        hallway[random_av_spot] = random_location[random_position]

                        if av_spots!=[]:
                            step += 1
                            value += energy(random_location[random_position])*((abs(random_av_spot-random_location[0])+1)+(1 if random_position==2 else 0))
                            #print(random_location[random_position], value, abs(random_av_spot-random_location[0]), random_av_spot, random_location[0])
                        random_location[random_position] = '.'

                    except:
                        pass
            else:
                outcome = go_to_room_from_hallway(random_location, random_position)
                if outcome[0] == 1:
                    step += 1
                    value += outcome[1]
        except:
            pass

    if room_1[1:]==['A', 'A'] and room_2[1:]==['B', 'B'] and room_3[1:]==['C', 'C'] and room_4[1:]==['D', 'D']:
        value_max = value if value<value_max else value_max
        print(value_max)

