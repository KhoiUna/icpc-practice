'''
1.6
https://open.kattis.com/problems/musicalscales?tab=metadata
'''
CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"] * 2

'''
`tonic` arg is the 1st note 
of the major scale
'''
def get_major_scale(tonic):
    do = CHROMATIC_SCALE.index(tonic)
    re = do + 2
    mi = re + 2
    fa = mi + 1
    sol = fa + 2
    la = sol + 2
    si = la + 2

    return [
        CHROMATIC_SCALE[do],
        CHROMATIC_SCALE[re],
        CHROMATIC_SCALE[mi],
        CHROMATIC_SCALE[fa],
        CHROMATIC_SCALE[sol],
        CHROMATIC_SCALE[la],
        CHROMATIC_SCALE[si]
    ]

input()
notes = set(input().split())

out = []
count = len(notes)

for tonic in CHROMATIC_SCALE:
    if tonic in out: break # `break` if the 2nd loop starts

    scale = get_major_scale(tonic)

    for note in notes:
        if note not in scale or count == 0: break
        count -= 1
        
    if count == 0:
        out.append(tonic)
    
    count = len(notes)


if len(out) == 0:
    print('none')
else:
    print(' '.join(out))