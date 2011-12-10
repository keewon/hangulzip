
table = {
    # common cho seong
    u'\u1100': 'G'  ,
    u'\u1101': 'Gg' ,
    u'\u1102': 'N'  ,
    u'\u1103': 'D'  ,
    u'\u1104': 'Dd' ,
    u'\u1105': 'R'  ,
    u'\u1106': 'M'  ,
    u'\u1107': 'B'  ,
    u'\u1108': 'Bb' ,
    u'\u1109': 'S'  ,
    u'\u110a': 'Ss' ,
    u'\u110b': ''   ,
    u'\u110c': 'J'  ,
    u'\u110d': 'Jj' ,
    u'\u110e': 'Ch' ,
    u'\u110f': 'K'  ,
    u'\u1110': 'T'  ,
    u'\u1111': 'P'  ,
    u'\u1112': 'H'  ,

    # common jung seong
    u'\u1161': 'a'  ,
    u'\u1162': 'ae'  ,
    u'\u1163': 'ya'  ,
    u'\u1164': 'yae'  ,
    u'\u1165': 'eo'  ,
    u'\u1166': 'e'  ,
    u'\u1167': 'yeo'  ,
    u'\u1168': 'ye'  ,
    u'\u1169': 'o'  ,
    u'\u116a': 'wa'  ,
    u'\u116b': 'wae'  ,
    u'\u116c': 'oe'  ,
    u'\u116d': 'yo'  ,
    u'\u116e': 'u'  ,
    u'\u116f': 'weo'  ,
    u'\u1170': 'we'  ,
    u'\u1171': 'wi'  ,
    u'\u1172': 'yu'  ,
    u'\u1173': 'eu'  ,
    u'\u1174': 'yi'  ,
    u'\u1175': 'i'  ,

    # common jong seong
    u'\u11a8': 'g'  ,
    u'\u11a9': 'gg'  ,
    u'\u11aa': 'gs'  ,
    u'\u11ab': 'n'  ,
    u'\u11ac': 'nj'  ,
    u'\u11ad': 'nh'  ,
    u'\u11ae': 'd'  ,
    u'\u11af': 'l'  ,
    u'\u11b0': 'lg'  ,
    u'\u11b1': 'lm'  ,
    u'\u11b2': 'lb'  ,
    u'\u11b3': 'ls'  ,
    u'\u11b4': 'lt'  ,
    u'\u11b5': 'lp'  ,
    u'\u11b6': 'lh'  ,
    u'\u11b7': 'm'  ,
    u'\u11b8': 'b'  ,
    u'\u11b9': 'bs'  ,
    u'\u11ba': 's'  ,
    u'\u11bb': 'ss'  ,
    u'\u11bc': 'ng'  ,
    u'\u11bd': 'j'  ,
    u'\u11be': 'ch'  ,
    u'\u11bf': 'k'  ,
    u'\u11c0': 't'  ,
    u'\u11c1': 'p'  ,
    u'\u11c2': 'h'  ,
}

def jamo_to_alphabet( text ):
    r = ''
    for c in text:
        if table.has_key(c):
            r = r + table[c]
        else:
            r = r + c

    return r
