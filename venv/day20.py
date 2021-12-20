
#image_enhancement = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
image_enhancement = '#....##..##...####...##.#..####..#.#.#.#..##....##....#.....#.##....##..###.#..####.#..#.###...##....##...#.#####..#.....#.#####.##....##..#.#####.....#.....###..#.#.###...###..#..#.#.#####....#.#..#..##..#.####.###.#.#...##.##.#.###...#####......#.........##.#.#####.##.##........#..#.##.####.#...#..#####.####.#.##.####.#.#.##.#..#..#.#....#.###.#.###.#......#..#...#.#..#..###..#....####...##....##.#..###...##.##.####..#..#..#..#.#...###.#.##.##.#..####.#.#..#....####......##.###.####..###.....##..##..##...'
def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append(line)
    return lines

def add_invisible_lines(lst, symbol):
    width = len(lst[0])
    new_line = symbol * width
    lst.append(new_line)
    lst.append(new_line)
    lst.insert(0, new_line)
    lst.insert(0, new_line)
    for ind, i in enumerate(lst):
        lst[ind] = symbol+symbol+i+symbol+symbol
    return lst

def output_pixel(lst):
    global image_enhancement
    new_lst = []
    for y, i in enumerate(lst):
        new_row = ''
        for x, j in enumerate(lst):
            if y!=0 and x!=0 and y!=len(lst)-1 and x!=len(lst[0])-1:
                coordinates=[(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x,y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
                coord_string = ''
                for k in coordinates:
                    coord_string += '1' if lst[k[1]][k[0]] == '#' else '0'
                coord_int = int(coord_string, 2)
                new_row += image_enhancement[coord_int]
            else:
                new_row += '.' if lst[y][x] == '#' else '#'
        new_lst.append(new_row)
    return new_lst


lst = read_file('input_day20.txt')

for n in range(0,50):
    print(n)
    symbol = '.' if n % 2 ==0 else '#'
    lst = add_invisible_lines(lst, symbol)
    lst = output_pixel(lst)

cnt = 0
for y, i in enumerate(lst):
    for x, j in enumerate(lst):
        if lst[y][x]=='#':
            cnt+=1
print(cnt)