import copy

def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            line = list(line)
            lines.append(line)
    return lines


def going_east(coordinates, row_length, map):
    if coordinates[0]==row_length-1:
        if map[coordinates[1]][0]=='.':
            return 'move', (coordinates[1], 0), 1
        else:
            return 'stop', (coordinates[1], coordinates[0]), 0
    else:
        if map[coordinates[1]][coordinates[0]+1]=='.':
            return 'move', (coordinates[1], coordinates[0]+1), 1
        else:
            return 'stop', (coordinates[1], coordinates[0]), 0

def going_south(coordinates, column_length, map):
    if coordinates[1]==column_length-1:
        if map[0][coordinates[0]]=='.':
            return 'move', (0, coordinates[0]), 1
        else:
            return 'stop', (coordinates[1], coordinates[0]), 0
    else:
        if map[coordinates[1]+1][coordinates[0]]=='.':
            return 'move', (coordinates[1]+1, coordinates[0]), 1
        else:
            return 'stop', (coordinates[1], coordinates[0]), 0

map = read_file('input_day25.txt')
row_length = len(map[0])
column_length = len(map)
cnt = 100
ind = 0
while cnt!=0:
    cnt = 0
    map_tmp = copy.deepcopy(map)
    for y, column in enumerate(map):
        for x, row in enumerate(column):
            if map[y][x] == '>':
                east = going_east((x,y), row_length, map)
                map_tmp[y][x] = '.'
                map_tmp[east[1][0]][east[1][1]] = '>'
                cnt += east[2]

    map = copy.deepcopy(map_tmp)
    for y, column in enumerate(map):
        for x, row in enumerate(column):
            if map[y][x] == 'v':
                south = going_south((x,y), column_length, map)
                map_tmp[y][x] = '.'
                map_tmp[south[1][0]][south[1][1]] = 'v'
                cnt += south[2]
    ind += 1
    map = copy.deepcopy(map_tmp)

print(ind)