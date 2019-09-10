from collections import namedtuple


Verse = namedtuple('Verse', ['day_index', 'gifts'])

verses = [
    None,
    Verse('first', 'a Partridge'),
    Verse('second', 'two Turtle Doves'),
    Verse('third', 'three French Hens'),
    Verse('fourth', 'four Calling Birds'),
    Verse('fifth', 'five Gold Rings'),
    Verse('sixth', 'six Geese-a-Laying'),
    Verse('seventh', 'seven Swans-a-Swimming'),
    Verse('eighth', 'eight Maids-a-Milking'),
    Verse('ninth', 'nine Ladies Dancing'),
    Verse('tenth', 'ten Lords-a-Leaping'),
    Verse('eleventh', 'eleven Pipers Piping'),
    Verse('twelfth', 'twelve Drummers Drumming'),
]


def get_gifts_for_day(day):
    gifts = []
    for idx in range(day, 0, -1):
        gifts.append(verses[idx].gifts)
    if len(gifts):
        gifts.append(f'and {verses[0].gifts}')
    else:
        gifts.append(verses[0].gifts)
    return gifts


def recite(start_verse, end_verse):
    song = []
    for day_no, verse in enumerate(verses[start_verse:end_verse]):
        gifts = ', '.join(get_gifts_for_day(day_no + start_verse))
        song.append(f'On the {verse.day_index} day of Christmas my true love gave to me: {gifts} in a Pear Tree.')
    return song
