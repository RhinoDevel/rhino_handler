
# Marcel Timm, RhinoDevel, 2022jul24

import random

PERSONS = [
        'Carolin',
        'ein Riesenfrosch',
        'Keet',
        'Hoakmoss',
        'Katharina',
        'Constantin',
        'Pittiplatsch',
        'Franziska',
        'Marcel',
        'Leonie',
        'Marinett',
        'Inga',
        'Elsa',
        'Teddy',
        'Jana',
        'Birke',
        'Juko',
        'Ontschao',
        'Alya',
        'Mia',
        'Willi Wonka',
        'Nora'
    ]

DOING = [
        'malen',
        'basteln',
        'spielen',
        'kaufen',
        'lachen über',
        'bewerfen',
        'gucken',
        'essen',
        'kitzeln',
        'jagen',
        'schimpfen über',
        'retten',
        'wären gern',
        'klauen',
        'schubsen',
        'verscheuchen',
        'bemalen',
        'reden über',
        'denken an',
        'kämpfen gegen',
        'hampeln wie',
        'hüpfen über',
        'heulen wie',
        'jammern wie',
        'sind verkleidet als',
        'gucken wie'
    ]

STUFF = [
        'Einhörner',
        'Bananen',
        'Klopapier',
        'Gummibärchen',
        'Würmer',
        'Sandalen',
        'Mettwurstbrot',
        'Bilder',
        'Pferde',
        'eine Frikadelle',
        'lila Monster',
        'Schuhe',
        'Hänsel und Gretel',
        'Lediback',
        'Elfen',
        'zwei Monster',
        'Kuchen',
        'Playmobil',
        'Zwergelefanten',
        'Unterhosen',
        'Ferkel',
        'die böse Hexe',
        'Gänse',
        'Jungs',
        'Mathe',
        'Oma und Opa',
        'Känguruhs',
        'Computer',
        'Marmelade',
        'Prinzessinnen',
        'Hammelbacken',
        'Ameisen',
        'Stinkekäse',
        'eine beleidigte Leberwurst',
        'ein Umpalummpa',
        'giftige Schlangen',
        'Würgeschlangen',
        'Dumbo',
        'Schneewittchen',
        'Rapunzel',
        'Dornröschen',
        'die Lego Fränts'
    ]

def exec(params):
    ret_val = None
    person_a = random.choice(PERSONS)
    person_b = None
    doing = random.choice(DOING)
    stuff = random.choice(STUFF)

    while True:
        person_b = random.choice(PERSONS)
        if person_b != person_a:
            break

    return f"{person_a} und {person_b} {doing} {stuff}"
