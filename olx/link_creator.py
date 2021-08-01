import itertools

part_one = ['https://www.olx.pl/nieruchomosci/mieszkania/wynajem/warszawa/']
part_two = [
    '?search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_0',
    '?search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_1&search%5Bfilter_enum_floor_select%5D%5B1%5D=floor_2',
    '?search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_3&search%5Bfilter_enum_floor_select%5D%5B1%5D=floor_4',
    '?search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_5&search%5Bfilter_enum_floor_select%5D%5B1%5D=floor_6'
    '&search%5Bfilter_enum_floor_select%5D%5B2%5D=floor_7&search%5Bfilter_enum_floor_select%5D%5B3%5D=floor_8'
    '&search%5Bfilter_enum_floor_select%5D%5B4%5D=floor_9&search%5Bfilter_enum_floor_select%5D%5B5%5D=floor_10'
    '&search%5Bfilter_enum_floor_select%5D%5B6%5D=floor_11'
]
part_three = [
    '&search%5Bfilter_enum_furniture%5D%5B0%5D=no',
    '&search%5Bfilter_enum_furniture%5D%5B0%5D=yes'
]
part_four = [
    '&search%5Bfilter_enum_builttype%5D%5B0%5D=blok',
    '&search%5Bfilter_enum_builttype%5D%5B0%5D=kamienica',
    '&search%5Bfilter_enum_builttype%5D%5B0%5D=wolnostojacy&search%5Bfilter_enum_builttype%5D%5B1%5D=szeregowiec',
    '&search%5Bfilter_enum_builttype%5D%5B0%5D=apartamentowiec&search%5Bfilter_enum_builttype%5D%5B1%5D=loft'
]
part_five = [
    '&search%5Bfilter_float_m%3Ato%5D=25',
    '&search%5Bfilter_float_m%3Ato%5D=35&search%5Bfilter_float_m%3Afrom%5D=26',
    '&search%5Bfilter_float_m%3Ato%5D=50&search%5Bfilter_float_m%3Afrom%5D=36',
    '&search%5Bfilter_float_m%3Afrom%5D=51'
]
part_six = [
    '&search%5Bfilter_enum_rooms%5D%5B0%5D=one',
    '&search%5Bfilter_enum_rooms%5D%5B0%5D=two',
    '&search%5Bfilter_enum_rooms%5D%5B0%5D=three',
    '&search%5Bfilter_enum_rooms%5D%5B0%5D=four'
]
file = open('list_of_links.txt', 'w')
# , part_three, part_four, part_five, part_six
list_of_links = list(itertools.product(part_one, part_two, part_three, part_four, part_five, part_six))
for link in list_of_links:
    full_link = ''.join(link)
    full_link = full_link + ' '
    file.write(str(full_link))